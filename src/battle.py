import sys
import time
from src import helper


def handle():

    start = time.time()
    stage = 1
    while(helper.isBattling()):
        if(isRewardScreen()):
            stage = stage + 1
            start = time.time()

        if((time.time() - start) > 300):
            print('>>> battle time expired, returning to main screen')
            start = time.time()
            backToMainScreen()
            return

        positions = getDepletedShipsInScreen()
        if(len(positions) > 4):
            time.sleep(5)
            backToMainScreen()
            return

        if(len(positions) > 1):
            time.sleep(20)
            backToMainScreen()
            return

        print('battling')

        helper.handlePopup()


def isRewardScreen():
    positions = helper.getImagePositions(
        'reward.png', 0.75)

    return len(positions) > 0


def backToMainScreen():
    retries = 3
    while(retries > 1):
        helper.handlePopup()
        time.sleep(2)
        helper.clickDestinationImage('battle-select-ships-button.png', 1, 0.8)
        retries = retries - 1


def getDepletedShipsInScreen():
    positions = helper.getImagePositions(
        'fighting-ship-depleted.png', 0.55)

    print('Depleted ships: ', len(positions))

    return positions
