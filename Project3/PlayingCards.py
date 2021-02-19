#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:56:57 2021

@author: sagarlamsal
"""
# Sagar Lamsal
#COMP3006: Python Software Development
#Project 3
# Card Game: Object Oriented Programming
import random


#card class that holds playing cards information

class card(object):                                            
    def __init__(self, cardSuit, val):
        self.cardSuit = cardSuit
        self.value = val
       
    
    def show(self):
        print (f'{self.value} of {self.cardSuit}')
        


#different suits of the cards

class deckOfCards(object):
    def __init__(self):
        self.cards = []
        self.buildDeck()
   
    
   
#entire deck of cards
  
    def buildDeck(self):
        for s in ["Clubs", "Diamonds", "Spades", "Heart"]:
            for v in range(1,14):
                self.cards.append(card(s,v))
#                print (f'{v} of {s}')
#            print (s)
   


#show the whole deck of cards

    def show(self):
        for c in self.cards:
            c.show()



#shuffle the deck

    def shuffleDeck(self):
        for i in range(len(self.cards)-1, 0, -1):
#            print (i)
            randomIndx = random.randint(0, i)
            self.cards[i], self.cards[randomIndx] = self.cards[randomIndx], self.cards[i]
  
    
 #draw cards from the deck
 
    def drawCards(self):
        return self.cards.pop()





class Player(object):
    def __init__(self, name):
       self.hand = []
       self.name = name


#player can draw a card from the deck      
    def draw(self, deck):
         self.hand.append(deck.drawCards())
         return self


#player can show his/her cards
    def showOfHands(self):
        for card in self.hand:
            card.show()


#player can discard a card
    def throw(self):
        return self.hand.pop()





'''
deck = deckOfCards()

deck.shuffleDeck()
deck.show()
'''

'''
sagar = Player("sagar")
sagar.draw(deck).draw(deck)
sagar.showOfHands()
'''


'''
card = deck.drawCards()
card.show()
'''
