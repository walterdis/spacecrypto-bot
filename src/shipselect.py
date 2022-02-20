from operator import le
from random import random, uniform
from time import sleep
from turtle import pos

import numpy as np
from src import helper, date
import pyautogui


def execute(screen):
    while(removeLowAmmo()):
        sleep(1)
        continue

    sleep(1)
    selectMaxAmmo()

    selectShips()

    sleep(1)


def selectShips():
    sleep(1)
    screen = helper.printSreen()

    isFull = False
    scrollAmount = 14
    while(not isFull):
        helper.handlePopup()
        sleep(1)
        screen = helper.printSreen()

        if(not helper.isShipSelectScreen(screen)):
            return False

        shipsInBattleEmpty = helper.getImagePositions(
            'main-ship-list-empty.png', 0.9, screen)

        print('Ships list is full ', helper.isShipsListFull(screen))
        print('Ships list is empty ', len(shipsInBattleEmpty) > 0)

        if(helper.isShipsListFull(screen)):
            startFight()
            break

        if(scrollAmount < 1):
            handleWaitOrFight()

        shipsAvailable = getFightPositionAvailable()
        print('Ships available: ', len(shipsAvailable))

        if(len(shipsAvailable) < 1):
            scrollsAvailable = scroll(scrollAmount)
            scrollAmount = scrollsAvailable
            print(scrollAmount, ' - ', scrollsAvailable)
            continue

        amount = 3
        while(amount > 0):
            if(helper.isShipsListFull()):
                break

            amount = amount-1

            x, y, w, h = shipsAvailable[0]
            helper.clickDestination(x+10, y+10, 1)

            print('selecting...')
            sleep(1)

            if(amount > 0):
                continue

            shipsAvailable = getFightPositionAvailable()

            if(len(shipsAvailable) > 0):
                amount = 2


def startFight():
    print('starting fight')
    helper.clickDestinationImage('fight-boss-button.png')
    sleep(3)
    helper.handleConfirm()


def scroll(amount=12):
    while(True):
        shipsAvailable = getFightPositionAvailable()

        if(len(shipsAvailable) > 0):
            return amount

        amount = amount - 1
        if(amount < 1):
            return 0

        screen = helper.printSreen()
        if(hasShipToFight(screen)):
            return amount

        fightUnavailablePositions = getFightPositionDisabled(screen)

        if(len(fightUnavailablePositions) < 1):
            print('Available ships not found!!!')
            return amount

        if(len(fightUnavailablePositions) > 1):
            scrollPosition = fightUnavailablePositions[1]
        else:
            scrollPosition = fightUnavailablePositions[0]

        x, y, w, h = scrollPosition
        pos_x = int(x+uniform(5, 25))
        pos_y = int(y+uniform(50, 100))

        helper.moveDestination(pos_x, pos_y, 1)
        #pyautogui.moveTo(x+50, y+100, 1)

        pyautogui.dragRel(0, -170, duration=1, button='left')
        sleep(2)


def removeLowAmmo():
    # @TODO implement better removal
    screen = helper.printSreen()
    positions = getShipsInBatleLowEnergy(screen)

    if(len(positions) < 1):
        print('Low ammo ships not found')
        return False

    print(len(positions), ' ships with low ammo found!')

    positions = np.flipud(positions)
    for (x, y, w, h) in positions:
        helper.clickDestination(x+110, y-5, 1)

    return True


def selectMaxAmmo():
    screen = helper.printSreen()
    maxPosition = helper.getImagePositions('combo-max-ammo.png', 0.9, screen)

    if(len(maxPosition) > 0):
        print('Correct ammo order already selected')
        return

    position = helper.getImagePositions('combo-newest.png', 0.9, screen)
    if(len(position) < 1):
        position = helper.getImagePositions('combo-min-ammo.png', 0.9, screen)

    if(len(maxPosition) > 0):
        print('Ammo order position not found!!!')
        return

    if(len(position) < 1):
        return

    x, y, w, h = position[0]
    helper.clickDestination(x+30, y+15, 2)

    sleep(1)
    screen = helper.printSreen()
    position = helper.getImagePositions(
        'combo-max-ammo-option.png', 0.9, screen)

    if(len(position) < 1):
        print('Max ammo option not found!!')
        return

    x, y, w, h = position[0]
    helper.clickDestination(x+30, y+10, 2)


def selectMinAmmo():
    screen = helper.printSreen()
    minPosition = helper.getImagePositions('combo-min-ammo.png', 0.9, screen)

    if(len(minPosition) > 0):
        print('Correct ammo order already selected')
        return

    position = helper.getImagePositions('combo-newest.png', 0.9, screen)
    if(len(position) < 1):
        position = helper.getImagePositions('combo-max-ammo.png', 0.9, screen)

    if(len(minPosition) > 0):
        print('Ammo order position not found!!!')
        return

    if(len(position) < 1):
        return

    x, y, w, h = position[0]
    helper.clickDestination(x+30, y+15, 2)

    sleep(1)
    screen = helper.printSreen()
    position = helper.getImagePositions(
        'combo-min-ammo-option.png', 0.9, screen)

    if(len(position) < 1):
        print('Min ammo option not found!!')
        return

    x, y, w, h = position[0]
    helper.clickDestination(x+30, y+10, 2)


def handleWaitOrFight():
    shipsInBattleFull = helper.getImagePositions(
        'main-ship-list-full.png', 0.95)

    if(len(shipsInBattleFull) > 0):
        startFight()

    shipsSelected = getShipsToRemove()
    if(len(shipsSelected) > 3):
        startFight()
        return

    removeAllShips()

    print('waiting for 20 minutes')
    sleep(1200)

    helper.clickDestinationImage('icon-base.png', 0.8)
    sleep(3)
    helper.clickDestinationImage('icon-spaceship.png', 0.8)

    return


def removeAllShips():
    if(not helper.isShipSelectScreen()):
        return

    while(True):
        shipsToRemove = getShipsToRemove()
        if(len(shipsToRemove) < 1):
            break

        shipsToRemove = np.flipud(shipsToRemove)

        for(x, y, w, h) in shipsToRemove:
            helper.clickDestination(x+5, y+5, 0.8)
            sleep(0.8)


def backToStageSelectAndWait():
    helper.clickDestinationImage('btn-back-stage-select.png')
    print(date.dateFormatted(), ' Waiting for near 2 hours...')
    sleep(7000)


def getFightPositionAvailable(screen=None):
    return helper.getImagePositions('ship-fight-button.png', 0.97, screen)


def hasShipToFight(screen=None):
    return len(getFightPositionAvailable(screen)) > 0


def getFightPositionDisabled(screen=None):
    return helper.getImagePositions('ship-fight-button-unavailable.png', 0.9, screen)


def getShipsInBatleLowEnergy(screen=None):
    return helper.getImagePositions('ship-list-low-energy.png', 0.85, screen)


def getShipsToRemove(screen=None):
    return helper.getImagePositions('ship-list-remove.png', 0.95, screen)
