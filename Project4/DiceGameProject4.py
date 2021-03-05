#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 3 19:25:34 2021

@author: sagarlamsal
"""

import random


#Dice class with operator overload for six different types
class Dice:                                             
    def __init__(self, sides):
        self.currentScore = int()
        self.sides = sides
        
        
#Creating comparison magic methods for six different operators
    def __eq__(self, other):
        return self.currentScore == other.currentScore

    def __ne__(self, other):
        return self.currentScore != other.currentScore

    def __lt__(self, other):
        return self.currentScore < other.currentScore 

    def __gt__(self, other):
        return self.currentScore > other.currentScore 

    def __le__(self, other):
        return self.currentScore <= other.currentScore

    def __ge__(self, other):
        return self.currentScore >= other.currentScore 
    
    
#Number of sides of dice and the current score of the dice
    def __str__(self):
        return f"Dice has {self.sides} and current score of {self.currentScore}"

    def add(self, value):
        self.currentScore += value

    def roll(self):
        self.add(random.randrange(1, self.sides + 1))



#Rolling the number of assigned dice and overload for six different operator types
class CupOfDice:
    def __init__(self, numOfDice, sides):
        self.numOfDice      = numOfDice 
        self.sides          = sides 
        self.diceObjects    = [Dice(self.sides)] * self.numOfDice
        self.currentScore   = int() 



#six different operator magic methods
    def __eq__(self, other):
        return self.currentScore == other.currentScore

    def __ne__(self, other):
        return self.currentScore != other.currentScore

    def __lt__(self, other):
        return self.currentScore < other.currentScore 

    def __gt__(self, other):
        return self.currentScore > other.currentScore 

    def __le__(self, other):
        return self.currentScore <= other.currentScore

    def __ge__(self, other):
        return self.currentScore >= other.currentScore 
    
    
    
#Total number of dice and the total sum of the dice score
    def __str__(self):
        return f"Total dices are {self.numOfDice} and current score is {self.currentScore}"

    def getWinner(self, other):
        if self > other:
            return 1
        elif self < other:
            return -1 
        else: 
            return 0

    def roll(self):
        for i in range(self.numOfDice):
            currObject = self.diceObjects[i]
            currObject.roll()
            self.currentScore += currObject.currentScore



def main():

    
#User chooses how many dice
    numOfDice   = int(input("How many dice[s] to roll : "))

#User chooses the sides of the dice
    numofSide   = int(input("How many side[s] in each dice : "))
    
    
#User inputs the stash amount they have with them
    totalBudget = int(input("Enter your initial budget : "))
    
#Setting the userInput value to 'Y' so that when the function is called, it can initiate and run the commads
    userInput    = 'Y'
    
    
    while totalBudget > 0 and userInput == 'Y':
        
            
            currentBet   = int(input("Enter your current bet : "))
    
            humanDice    = CupOfDice(numOfDice, numofSide)
            computerDice = CupOfDice(numOfDice, numofSide)
    
            humanDice.roll()
            computerDice.roll() 
    
            print(humanDice)
            print(computerDice)
    
            if humanDice.getWinner(computerDice) == -1:
                print("Computer wins")
                totalBudget -= currentBet
            elif humanDice.getWinner(computerDice) == 1:
                print("Human wins")
                totalBudget += currentBet
            else:
                print("It's a draw")
    
            print(f"Remaining budget is {totalBudget}")
            
#placing this here so that when the user inputs 'n', the program doesn't run the loop once again before exiting
#because the loop always starts with 'Y' so that the funtion can run. 
            userInput    = input("Want to play ? (Y/N) : ").strip().upper()

#Calling the main() function so the program can initiate 
main()
