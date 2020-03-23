import mss, mss.tools

import numpy as np

from common import Rectangle


# Take a screenshot for the whole (1920 x 1080) screen
# Returns a numpy array of the screenshot
def capture():
    return capture(Rectangle(0, 0, 1920, 1080))


# Take a screenshot for the specified AOI
#  aoi: a common.Rectangle
# Returns a numpy array of the screenshot
def capture(aoi):
    monitor = {"top": aoi.y, "left": aoi.x, "width": aoi.w, "height": aoi.h}
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)
        return np.array(sct_img)