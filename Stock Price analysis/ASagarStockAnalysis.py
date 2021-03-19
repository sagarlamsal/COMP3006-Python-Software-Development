#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:20:01 2021

@author: sagarlamsal
"""


import matplotlib.pyplot as plt
import pandas as pd
import nltk.sentiment.vader

from matplotlib.pyplot import figure
from  nltk.sentiment.vader import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen

finviz_url = 'https://finviz.com/quote.ashx?t='

#tickers = ['AAPL', 'GOOG', 'MSFT']
tickers = ['TSLA', 'GOOG', 'MSFT']
#tickers = ['JPM', 'BAC', 'MS']           # Banks and financial institutions




news_tables = {}

for ticker in tickers:
    url = finviz_url + ticker
    
    
    req = Request(url = url, headers = {'user-agent': 'saag-app'})
    response = urlopen(req)
    #print(response)
    
    html = BeautifulSoup(response, 'html')
    #print(html)
    
    news_table = html.find(id = 'news-table')
    news_tables[ticker] = news_table
    
    



# =============================================================================
# tsla_table = news_tables['TSLA']
# tsla_rows = tsla_table.findAll('tr')
# #print(tsla_rows)
# 
# for index, row in enumerate(tsla_rows):
#     title = row.a.text  #anker tag in the table row
#     #print(title)
#     
#     timestamp = row.td.text
#     #print(timestamp + "" + title)
# 
# 
# 
# goog_table = news_tables['GOOG']
# goog_rows = goog_table.findAll('tr')
# #print(goog_rows)
# 
# for index, row in enumerate(goog_rows):
#     title = row.a.text  #anker tag in the table row
#     #print(title)
#     
#     timestamp = row.td.text
#     #print(timestamp + "" + title)
# 
# 
# 
# msft_table = news_tables['MSFT']
# msft_rows = msft_table.findAll('tr')
# #print(msft_rows)
# 
# for index, row in enumerate(msft_rows):
#     title = row.a.text  #anker tag in the table row
#     #print(title)
#     
#     timestamp = row.td.text
#     #print(timestamp + "" + title)
# =============================================================================


parse_data = []

for ticker, news_table in news_tables.items():
    
    for row in news_table.findAll('tr'):
        
        title = row.a.text
        dates = row.td.text.split(' ')       #split it based on space between the texts
        
        if len(dates) == 1:
            time = dates[0]
        else:
            date = dates[0]
            time = dates[1]
            
            parse_data.append([ticker, date, time, title])


#print(parse_data)





# =============================================================================
# 
# newsParse = []
# for file_name, newsTable in tableOfNews.items():
#     
#     #iterate through all the 'tr' tags in the news_table
#     for x in newsTable.find_all("tr"):
#         
#         #read the text from each tr tag into a text
#         text = x.a.get_text()
#         
#         #split the 'td' tag text into a list
#         scrapeData = x.td.text.split()
#         
#         #if the length is 1, the time will be the only element
#         if len(scrapeData) == 1:
#             time = scrapeData[0]
#          
#         #if not then date will be saved as the first element and time as the second element
#         else:
#             date = scrapeData[0]
#             time = scrapeData[1]
#          
#             
#          #extracting the ticker from the file_name
#         ticker = file_name.split('_')[0]
#         
#         
#         
#         #append the extrated data as a list
#         newsParse.append([ticker, date, time, text])
#         
# newsParse
# 
# =============================================================================


df = pd.DataFrame(parse_data, columns = ['ticker', 'date', 'time', 'title'])
#print(df.head())           #first 5 rows only






vader = SentimentIntensityAnalyzer()

#print(vader.polarity_scores("I love Tesla. They are the best in electric car company and everyone likes Tesla for making such a great all-elctric car. Kudos to Tesla."))


#print(df['title'])






f = lambda title: vader.polarity_scores(title)['compound'] #lambda function which gives only the compound score
df['compound'] = df['title'].apply(f)


#print(df.head())


df['date'] = pd.to_datetime(df.date).dt.date        #convert from string to date time format

plt.figure(figsize = (10,8))

mean_df = df.groupby(['ticker', 'date']).mean()  #returns the colum ticker, colum date and mean value of the compound value

mean_df = mean_df.unstack()         #allows to have dates as x-axis
mean_df = mean_df.xs('compound', axis = 'columns').transpose()      #xs -> cross section

#print(mean_df)


mean_df.plot(kind= 'bar')
plt.show()

