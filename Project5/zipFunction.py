#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:03:33 2021

@author: sagarlamsal
"""

# Sagar Lamsal

# Zip Function Set of deck of cards



# I made two deck of cards. One just a regular deck of cards and the other one...
#...has its corresponding hand values while playing Black Jack, which I got from Google... 
#...and I am not entirely sure are the correct values as I have never played Black Jack.


print("\n This is a standard deck of cards. \n")

suits = ['♠', '♥', '♦', '♣']
values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
for i in range(len(suits)):         #runs the for loop until it passes through all the elements in the suits list.
    deck = [[suits[i] for j in range(13)], values]      #iterates the suits and values together until the for loop completes it function.
    setDeck = zip(*deck)
    print(tuple(setDeck))       #creates the list of tuples of a standard set of cards.






print("\n Below are the deck of cards and values for playing Black Jack. \n")

suits = ['♠', '♥', '♦', '♣']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck = [(c, s, v)  for c,v in zip(cards, values) for s in suits] #zips the cards and values with all the elements from the suits. 
print (deck) 




