#!/usr/bin/python3

__author__ =  'Wyatt Hoffman'

# Rock, Paper, Scissors

# Import Modules
import random

# Main Method
def main():
    print('Welcome to Rock, Paper, Scissors!')
    print('---------------------------------')
    pName = playerInfo()
    pChoice = playerChoice()
    cChoice = cpuChoice()
    outcome(pName, pChoice, cChoice)
    playAgain = input('Play again? (Y/N): ')
    print()
    while True:
        if playAgain == 'Y':
            print('Welcome to Rock, Paper, Scissors!')
            print('---------------------------------')
            pChoice = playerChoice()
            cChoice = cpuChoice()
            outcome(pName, pChoice, cChoice)
            playAgain = input('Play again? (Y/N): ')
            print()
            continue
        else:
            print("Thanks for playing!")
            break

# Other Methods
def mainMenu():
    gameOptions = ['New Game', '']

def playerInfo():
    playerData = []
    newPlayer = input('Player 1 input your name')
    return playerData[1]

def playerChoice():
    while True:
        playerOneChoice = input('Select your move (R = Rock, P = Paper, S = Scissors): ')
        if playerOneChoice == 'R' or playerOneChoice == 'P' or playerOneChoice == 'S':
            break
        else:
            print('Invalid Choice, please choose R, P, or S')
            continue
    return playerOneChoice

def cpuChoice():
    cpuChoice = random.choice(['R', 'P', 'S'])
    return cpuChoice


def outcome(pName, pChoice, cChoice):
    if pChoice == cChoice:
        print('Tie')
    elif pChoice == 'R' and cChoice == 'P':
        print(pName + " Loses!")
    elif pChoice == 'R' and cChoice == 'S':
        print(pName + " Wins!")
    elif pChoice == 'P' and cChoice == 'S':
        print(pName + " Loses!")
    elif pChoice == 'P' and cChoice == 'R':
        print(pName + " Wins!")
    elif pChoice == 'S' and cChoice == 'R':
        print(pName + " Loses!")
    else:
        print(pName + " Wins!")

if __name__ == "__main__":
    main()