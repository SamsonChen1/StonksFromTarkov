import logging
import time
import Engine

import sys


def main():

    # TODO arg parsing
    # TODO options other than just running; e.g. show stats
    item = sys.argv[1]

    engine = Engine()

    # TODO exit condition
    # TODO gui
    while True:
        engine.run()


if __name__ == "__main__":
    main()
