# -*- coding: utf-8 -*-
from cv2 import cv2

from os import listdir
from random import randint, uniform
from random import random

import numpy as np
import pyautogui
import time
import sys
from src import login, helper, shipselect, date, battle


#pyautogui.PAUSE = pause
pyautogui.FAILSAFE = False

wolf = """
                                                                  .
                                                                 / V\\
                                                               / `  /
                                                              <<   |
                                                              /    |
                                                            /      |
                                                          /        |
                                                        /    \  \ /
                                                       (      ) | |
                                               ________|   _/_  | |
                                             <__________\______)\__)
=========================================================================
======================== LUS BUSD BNB USDT USDC =========================
============== 0x1F66230C4e98b557D3e55d7d2C047CcbA8E55bD6 ===============
=========================================================================
============== https://github.com/walterdis/spacecrypto-bot ================
=========================================================================
"""


print(wolf)
time.sleep(3)


def main():

    time.sleep(1)

    start = time.time()
    while True:
        helper.handleConfirm()
        helper.handleAfterBattleConfirm()
        helper.handlePopup()


        screen = helper.printSreen()
        
        if(isLoginScreen(screen)):
            print('Login screen found!!!')
            login.doLogin()

        screen = helper.printSreen()
        if(helper.isShipSelectScreen(screen)):
            print('Ship select screen found!!!')
            shipselect.execute(screen)
            time.sleep(2)
            helper.handleConfirm()

        battle.handle()
            
        helper.handleAfterBattleConfirm()
        helper.clickDestinationImage('play-button.png', 'play-button', 2)

        print('waiting ...')

        time.sleep(1)


def isLoginScreen(screen):
    positions = helper.getImagePositions('connect-wallet.png', 0.7, screen)

    return len(positions) > 0

main()
