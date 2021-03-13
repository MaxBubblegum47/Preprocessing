#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:16:06 2020

@author: lorenzostigliano
"""
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("/Users/lorenzostigliano/Desktop/Lyrics copia/Avicii/3 Million (Your Love Is So Amazing)_Avicii.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()

with open("/Users/lorenzostigliano/Desktop/Progetto Gestione dell'Informazione/Search Engine/filteredtext.txt", "r") as f:
    with open("/Users/lorenzostigliano/Desktop/Lyrics copia/Avicii/3 Million (Your Love Is So Amazing)_Avicii.txt", "w") as f1:
        for line in f:
            f1.write(line)

import os
os.remove("/Users/lorenzostigliano/Desktop/Progetto Gestione dell'Informazione/Search Engine/filteredtext.txt")
