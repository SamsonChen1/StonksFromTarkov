import logging
import time

from io import (
    ScreenshotManager,
    Robot,
    Serde
)
from common import (
    Constants,
    Rectangle,
    Trader,
    Offer,
    Ask,
    Purchase
)
from ocr import Reader
from model.PricingModel import PricingModel
from model.FeeModel import FeeModel


class Engine():

    # TODO move these location constants to commons #
    def ask_aoi(self):
        # TODO
        return Rectangle(-1, -1, -1, -1)

    def purchase_button_location(self):
        # TODO
        return [-1, -1]

    def purchase_all_location(self):
        # TODO
        return [-1, -1]

    def get_current_trader(self):
        # TODO
        return Trader(-1, -1)

    def did_buy_succeed(self):
        # TODO take a screenshot and check
        return False

    def buy_lowest_ask(self):
        # TODO use Robot to buy
        Robot.move_relative(*self.purchase_button_location())
        Robot.click()
        Robot.move_relative(*self.purchase_all_location())
        Robot.click()
        Robot.type('y')
        return self.did_buy_succeed()

    def sell_first_item(self, price):
        # TODO use Robot to sell
        pass

    def __init__(self):
        # TODO define contract
        self.pricing_model = PricingModel(-1)
        pass

    def run(self):
        # Check for asks 3
        ask_screenshot = ScreenshotManager.capture(self.ask_aoi())
        current_asks = Reader.get_asks(ask_screenshot)

        # Actions #
        # Check if we should buy #
        lowest_ask = min(current_asks, key=lambda x: x.price)
        if lowest_ask.price < self.pricing_model.confidence_interval(Constants.PURCHASE_INTERVAL):
            if not self.buy_lowest_ask():
                logging.info("Failed to make a purchase!")
            else:
                Robot.long_sleep()
                # Sell #
                self.sell_first_item(self.pricing_model.confidence_interval(Constants.SELL_INTERVAL))
                # TODO finish this logic

        # Record keeping #
        # TODO bg these
        PricingModel.update(self.asks)
        for a in current_asks:
            Serde.record_ask(a)
