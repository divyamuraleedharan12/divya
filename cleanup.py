# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import clean_up as cl

help(cl.clean)

text = open("big_data.txt")
print(text)
text_df = pd.read_csv("big_data.txt",sep="/s")
print(text_df)

all_words = []
counter = 0
for line in text:
    words = line.split()
    counter += 1
    for word in words:
        word = cl.clean(word)
        all_words.append(word)
        print(all_words)
        
df_words = pd.DataFrame(data=all_words,columns=("words",))
print(df_words)
df_counts= df_words.value_counts()
print(df_counts)

df_counts.to_csv("wordscount.csv")
print(len(all_words))

nchar = 0
for word in all_words:
    nchar = nchar + len(word)
    print(nchar)
    
    
all_letters = []
counter = 0
for line in text:
    words = line.split()
    counter += 1
   
    for word in words:
        word=cl.clean(word)
        letters = listr(word)
       for l in letters:
           
           all_letters.append(l)
    print(all_letters)
           
       
        

