from common import (
    Constants,
    Rectangle,
    Trader,
    Offer,
    Ask,
    Purchase
)
from io import (
    ScreenshotManager,
    Robot
)


PACKETS = "packets"
SCREEN_AND_MOUSE = "screen_and_mouse"


class PurchaseResult():
    SUCCESS = "success"
    FAILURE = "failure"
    UNKNOWN = "unknown"

def IoManager(mode):
    if mode == SCREEN_AND_MOUSE:
        return ScreenAndMouseIoManager()
    elif mode == PACKETS:
        raise Exception("Not implemented") # TODO
    else:
        raise Exception("Unknown Mode")

# TODO find AOI constants
# TODO implement stubs
class ScreenAndMouseIoManager():

    ASK_AOI = Rectangle(-1, -1, -1, -1)
    PURCHASE_BUTTON = [-1, -1]
    TRADER_AOI = Rectangle(-1, -1, -1, -1)

    def get_asks(self):
        return [Ask(-1, -1, -1, -1)]

    def get_fee(self):
        return -1

    def get_trader(self):
        return Trader(-1, -1)

    def did_buy_succeed(self):
        return PurchaseResult.FAILURE

    def buy_lowest_ask(self):
        Robot.move_relative(*self.PURCHASE_BUTTON)
        Robot.click()
        Robot.type('y')
        result = PurchaseResult.UNKNOWN
        while result == PurchaseResult.UNKNOWN:
            result = self.did_buy_succeed()
            Robot.long_sleep(0.5)
        return result

    def sell_first_item(self, price):
        # TODO use Robot to sell
        pass

    def wait(self, seconds=2):
        Robot.long_sleep(seconds)
