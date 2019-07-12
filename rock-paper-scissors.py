#!/usr/bin/python3

__author__ =  'Wyatt Hoffman'

# Rock, Paper, Scissors

# Import Modules
import random

# Main Method
def main():
    login()
    pName = playerData()
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
def login():
    print('Welcome to Rock, Paper, Scissors!')
    print('---------------------------------')
    playerType = input('New or Existing Player? (Press N for New or E for Existing): ')
    if playerType == 'N':
        playerData()


def playerData():
    players = {}
    while True:
        newPlayer = input('Input your Username: ')
        if newPlayer in players:
            print('Username already exists')
            continue
            while True:
            password = input('Input your Password (Minimum 8 Characters): ')
            if len(password) < 8:
                print("Password did not meet 8 character requirement")
                continue
            else:
                break

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
