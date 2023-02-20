#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:14:42 2023

@author: roshanrichard
"""
import clean_up as cl
import pandas as pd



text = open('big_data.txt','r')
#print(text.read())
all_words = []
all_letters = []
counter = 0
l_word = ''
test_counter = 0

for line in text:
   # print(line)
   # print("ff")
    words = line.split()
    counter += 1
    
    for word in words:
        word = cl.clean(word)
        
        if len(word) > len(l_word):
            
            test_counter = counter
        
            l_word = word
        all_letters = all_letters + list(word)
        all_words.append(word)


df_words = pd.DataFrame(data=all_words, columns=("words",))
df_counts = df_words["words"].value_counts()

df_letters = pd.DataFrame(data = all_letters, columns = ("letters",))
df_counts_letters = df_letters["letters"].value_counts()

df_counts.to_csv("wordcount.csv")

print(len(all_letters))
print(df_counts_letters)
print(df_counts)

print("number of unique words in the file is : " + str(len(df_counts)))
print("number of lines in the file is : " + str(counter))
print( "number of total words in the file is : " + str(len(df_words))+"\n")

print(l_word , test_counter)

print(df_counts_letters['d'])



#df = pd.read_csv(temp,sep = " ")

#print(outfile)
#print(df)