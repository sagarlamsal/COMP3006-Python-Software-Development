#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:04:59 2021

@author: sagarlamsal
"""

import numpy as np
import pandas as pd

random_matrix_array = np.random.randint(0,101, size=(10001,10))


#print(random_matrix_array)

np.savetxt('Grades.csv', random_matrix_array, fmt = '%10.5f', delimiter = ',')

#importing the CSV file as a dataframe using pandas

df1 = pd.read_csv(r'Grades.csv')

#giving the columns header
df = pd.DataFrame(random_matrix_array, columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])


#print(df.columns)
#list(random_matrix_array.columns)

#calculating the mean
df_mean = df[['a','b','c','d','e','f','g','h','i','j']].mean()
#print(df_mean)

#calculating the median
df_median = df[['a','b','c','d','e','f','g','h','i','j']].median()
#print(df_median)

#calculating the mode
df_modes = df[['a','b','c','d','e','f','g','h','i','j']].mode()
#print(df_modes)


# =============================================================================
# the mode function was working fine but once I completed the whole program, 
# it started giving me 3 rows of data and it stopped writing it on the .txt file. 
# I tried multiple times to make it work, but I couldn't get  it to write into .txt file.
# it gives the value while priting, but the output is weird. 
# Just wanted to inform. 
# =============================================================================


#calculating the standard deviation
df_std = df[['a','b','c','d','e','f','g','h','i','j']].std()
#print(df_std)





#get 3 different rows of user's choosing
def random_rows(filePath, row_indices=[]):

    with open(filePath) as file_csv:

       
        for i, line in enumerate(file_csv):  #track the line number from the file
            if i in row_indices:
 
               yield line

row_generation = random_rows('Grades.csv', row_indices = [10, 551, 999])
the_rows = np.loadtxt(row_generation, delimiter=",")           
#print(the_rows)

#change the array to string to write into .txt file
to_str = [','.join(item) for item in the_rows.astype(str)]
#print(to_str)



#part 4: writing into text file

with open("project6.txt", "w+") as file_handler:
    file_handler.write("THE MEAN IS: \n\n" )
    for item in df_mean:
        file_handler.write(f'{item}\n')
    
    file_handler.write("\n\n\n THE MEDAIN IS: \n\n")
    for item in df_median:
        file_handler.write(f'{item}\n')
    
    file_handler.write("\n\n\n THE MODE IS: \n\n")
    for item in df_modes:
        file_handler.write(f'{item}\n')
        
    file_handler.write("\n\n\n THE STANDARD DEVIATION IS: \n\n")
    for item in df_std:
        file_handler.write(f'{item}\n')
    
    file_handler.write("\n\n\n\n These are the column-names of the matrix.\n\n")
    for item in list(df.columns):
        file_handler.write("%s\n" %item)
    
    file_handler.write("\n\n\n\n These are the 3 rows of my choosing:\n\n")
    for listitem in to_str:                     #tried a different approach to write the list into the .txt file and it worked.
        file_handler.write('%s\n' % listitem)
    
file_handler.close()


