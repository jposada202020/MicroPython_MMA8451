# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_mma8451 import mma8451

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
mma = mma8451.MMA8451(i2c)

mma.high_pass_filter = mma8451.HPF_ENABLED
mma.high_pass_filter_cutoff = mma8451.CUTOFF_8HZ

while True:
    for high_pass_filter_cutoff in mma8451.high_pass_filter_cutoff_values:
        print("Current High pass filter cutoff setting: ", mma.high_pass_filter_cutoff)
        for _ in range(10):
            accx, accy, accz = mma.acceleration
            print("x:{:.2f}m/s2, y:{:.2f}m/s2, z:{:.2f}m/s2".format(accx, accy, accz))
            print()
            time.sleep(0.5)
        mma.high_pass_filter_cutoff = high_pass_filter_cutoff
