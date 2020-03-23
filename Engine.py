import logging
import time
from common import (
    Constants,
    Rectangle,
    Trader,
    Offer,
    Ask,
    Purchase
)
from io import Serde
from model.PricingModel import PricingModel
from model.FeeModel import FeeModel


class Engine():

    def __init__(self, item, io_manager):
        self.item = item
        self.io = io_manager
        self.asks = Serde.get_asks(self.item)
        self.trader = self.io.get_trader()
        self.offers = Serde.get_offers(self.item)

        # Models
        self.pricing_model = PricingModel(self.asks)
        self.fee_model = FeeModel(self.pricing_model, self.offers)

    def should_purchase(self, price, sell_price):
        return self.fee_model.predict(price) + price < sell_price

    def run(self):
        current_asks = self.io.get_asks()

        # Actions #
        # Check if we should buy #
        lowest_ask = current_asks[0]
        second_lowest_ask = current_asks[1]
        if self.should_purchase(lowest_ask.price, second_lowest_ask):  # TODO do we want to sell higher?
            if not self.io.buy_lowest_ask():
                logging.info("Failed to make a purchase!")
            else:
                logging.info("Made a purchase")
                while self.trader.offer_count >= Constants.MAX_OFFERS:
                    logging.info("Max offers already placed, can't sell yet...")
                    self.io.wait(10)
                offer = self.io.sell_first_item(second_lowest_ask - 1)
                if not offer:
                    raise Exception("Failed to make an offer!")
                else:
                    logging.info("Placed an offer")
                    Serde.record_offer(offer)  # TODO bg this
                    Serde.record_trader(self.trader)  # TODO bg this
                    self.trader = self.io.get_trader()

        # Record keeping #
        # TODO bg these
        self.pricing_model.update(self.asks)
        self.fee_model.update(self.pricing_model, self.asks)
        for a in current_asks:
            Serde.record_ask(a)
