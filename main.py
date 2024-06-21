import random

class Dice:
    maxDiceRoll = 0
    numberOfDice = 0
    def __init__(self, max, number):
        self.maxDiceRoll = max
        self.numberOfDice = number

    def roll(self):
        diceRoll = random.randint(1, self.maxDiceRoll)
        return diceRoll

    def rollDice(self):
        diceRoll = 0
        temp = 0
        for i in range(0, self.numberOfDice):
            temp = self.roll()
            print("Dice roll:  " + str(temp))
            diceRoll += temp
        return diceRoll

def anaylyzeUserInput(input):
    str = input.split('d')
    dice = Dice(int(str[1]), int(str[0]))
    total = dice.rollDice()
    return total

if __name__ == '__main__':
    inp = input("Enter a number ( Example 1d20 stands for 1 dice of 20 ): ")
    print(str(anaylyzeUserInput(inp)))