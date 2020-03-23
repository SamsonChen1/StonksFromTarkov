# Stores various common constants
class Constants():
    from model import Confidence
    PURCHASE_INTERVAL = Confidence.BAND_P01
    SELL_INTERVAL = 0.75


# Data type used to describe a rectangle
class Rectangle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

# Data type used to represent an offer.
# id is the unique ID of the item, used to identify a later offer on this same item.
# ts is the timestamp of the purchase
class Purchase():
    def __init__(self, id, item, price, ts):
        self.id = id
        self.item = item
        self.price = price
        self.ts = ts

    def serialize(self):
        return f"{self.id}|{self.item}|{self.price}|{self.ts}"

    @staticmethod
    def deserialize(s):
        return Purchase(*s.split('|'))


# Data type used to represent an offer placed by the trader:
# id is the unique ID of the item, used to identify an earlier purchase of the same item.
# open_ts is the timestamp of the offer being opened
# close_ts is the timestamp of the offer being closed
class Offer():
    def __init__(self, id, item, price, fee, open_ts, close_ts):
        self.id = id
        self.item = item
        self.price = price
        self.fee = fee
        self.open_ts = open_ts
        self.close_ts = close_ts

    def serialize(self):
        return f"{self.id}|{self.item}|{self.price}|{self.fee}|{self.open_ts}|{self.close_ts}"

    @staticmethod
    def deserialize(s):
        return Offer(*s.split('|'))


# Data type used to represent an open ask on the market:
# id is a unique ID used to identify the same ask across observations.
# ts is the timestamp when the ask was observed
class Ask():
    def __init__(self, id, item, price, ts):
        self.id = id
        self.item = item
        self.price = price
        self.ts = ts

    def serialize(self):
        return f"{self.id}|{self.item}|{self.price}|{self.ts}"

    @staticmethod
    def deserialize(s):
        return Ask(*s.split('|'))

# Data type used to represent the trader:
class Trader():
    def __init__(self, balance, offer_count):
        self.balance = balance
        self.offer_count = offer_count

    def serialize(self):
        return f"{self.balance}|{self.offer_count}"

    @staticmethod
    def deserialize(s):
        return Trader(*s.split('|'))
