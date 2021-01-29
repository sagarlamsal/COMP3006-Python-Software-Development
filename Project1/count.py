#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:46:29 2021

@author: sagarlamsal
"""

# Sagar Lamsal
# DU- iD: 873556973
# This program counts characters in a .txt file. 
# It has different flags which are used to interpret how the program outputs the final result.


import sys

def add_frequencies(d,file,remove_case):
    
    with open(file) as f:                           # opens the .txt file specified in the command line
        for line in f:
            line = line.rstrip()                    # removes the new line count so the frequency of new line doesn't get counted.
            if remove_case:
                line = line.lower()                 # makes every character into a lower case depending whether the remove_case is true or false.
            for char in line:
                if char in d:
                    d[char] += 1                    
                else:
                    d[char] = 1
    f.close()
    return(d)

def printColumn(d):
    for key, value in d.items():
        print("\"{0}\", {1}".format(key,value))


def main():
    
    remove_case = True                              # since the remove_case is specified as true, the program is going to change the characters in the file to all lower case as specified above.
    numberArg = len(sys.argv)                       # gets the length of the system argument. 
    filename = str(sys.argv[numberArg-1])           # specifies which part of the argument is to be considered as the file name.
    
    
    flag=""
    if numberArg>2:                                 # specifies that if there are no flags present in the command line, then run the file 
        flag = sys.argv[1]
                                
        
        
    d={}                                            # creating an empty dictionary d to store values/characters
    if flag=='-c':                                  # a -c flag reads the characters as it is. 
        remove_case=False                           # when remove_case is False, the program will read the character as it is and prints the output without any alteration of the characters in the file.
        
        
    elif flag =='-z':                               # a -z flag will output all the alphabets in the english language while giving the frequencies of the characters available in the .txt file. 
        d={'a':0,
           'b':0,
           'c':0,
           'd':0,
           'e':0,
           'f':0,
           'g':0,
           'h':0,
           'i':0,
           'j':0,
           'k':0,
           'l':0,
           'm':0,
           'n':0,
           'o':0,
           'p':0,
           'q':0,
           'r':0,
           's':0,
           't':0,
           'u':0,
           'v':0,
           'w':0,
           'x':0,
           'y':0,
           'z':0}
        
        remove_case=True
        
        
    elif flag =='-l':                               # a -l flag has another set of instructions attached with it. 
        inputChar = str(sys.argv[2]).lower()         
        remove_case=True
        
    
    elif flag =='':                                 # simple error checking function, so when someone accidentally enters an undefined flag, it shows up as an error.
        pass
    else:
        return print("The flag does not exist. The supported flags are -c -z -l)")
    
    
    
    out = add_frequencies(d, filename, remove_case) # calls the add_frequencies function for the -l flag
    if flag == '-l':
        out2={}
        for char in inputChar:
            out2[char]=out[char]                    # stores the given command for -l flag into out2 dictionary and compares it to the out[] to see if they both have same characters
        printColumn(out2)                       # if -l flag characters and out[] dictionary characters match, the funtion prints out the frequency of the out2[] dictionary characters.
    else:
        printColumn(out)                                  # if there are no characters specified for the -l flag, the system just prints out the frequencies of the all the characters in the .txt file. 
    

if __name__=="__main__":                            # check if the main() function is in the primary file and if it is true then it runs the main function. 
    main()