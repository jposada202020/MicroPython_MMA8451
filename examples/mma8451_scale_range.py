# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_mma8451 import mma8451

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
mma = mma8451.MMA8451(i2c)

mma.scale_range = mma8451.RANGE_8G

while True:
    for scale_range in mma8451.scale_range_values:
        print("Current Scale range setting: ", mma.scale_range)
        for _ in range(3):
            accx, accy, accz = mma.acceleration
            print("x:{:.2f}m/s2, y:{:.2f}m/s2, z:{:.2f}m/s2".format(accx, accy, accz))
            print()
            time.sleep(0.5)
        mma.scale_range = scale_range
