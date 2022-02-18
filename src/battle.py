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
            print('battle time expired, returning to main screen')
            start = time.time()
            backToMainScreen()
            return

        positions = getDepletedShipsInScreen()
        if(len(positions) > 1):
            time.sleep(20)
            backToMainScreen()
            return

        sys.stdout.flush()
        print('battling')

        helper.handlePopup()

       # time.sleep(1)


def isRewardScreen():
    positions = helper.getImagePositions(
        'reward.png', 0.75)

    return len(positions) > 0


def backToMainScreen():
    helper.clickDestinationImage(
        'battle-select-ships-button.png', 'battle-select-ships-button', 1, 0.8)


def getDepletedShipsInScreen():
    positions = helper.getImagePositions(
        'fighting-ship-depleted.png', 0.55)

    print('Depleted ships: ', len(positions))

    return positions
