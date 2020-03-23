from common import (
    Purchase,
    Offer,
    Ask,
    Trader
)

def record_purchase(purchase):
    with open(f"data/purchases/{purchase.item}.dat", "w") as file:
        file.write(purchase.serialize())


def record_offer(bid):
    with open(f"data/offers/{bid.item}.dat", "w") as file:
        file.write(bid.serialize())


def record_ask(ask):
    with open(f"data/asks/{ask.item}.dat", "w") as file:
        file.write(ask.serialize())


def record_trader(trader):
    with open(f"data/trader.dat", "w") as file:
        file.write(trader.serialize())


def get_purchases(item):
    with open(f"data/purchases/{item}.dat", "r") as file:
        return list(map(lambda x: Purchase.deserialize(x), file.readlines()))


def get_offers(item):
    with open(f"data/offers/{item}.dat", "r") as file:
        return list(map(lambda x: Offer.deserialize(x), file.readlines()))


def get_asks(item):
    with open(f"data/asks/{item}.dat", "r") as file:
        return list(map(lambda x: Ask.deserialize(x), file.readlines()))


def get_traders():
    with open(f"data/trader.dat", "r") as file:
        return list(map(lambda x: Trader.deserialize(x), file.readlines()))
