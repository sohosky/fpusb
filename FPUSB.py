# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 21:12:21 2021

@author: SKY
"""

import usb.core
import usb.util

dev = usb.core.find(idVendor=0x04f3)

if dev is None:
    print('-----No find device----')
else:
    print('----Find Elan FP Device----')
    