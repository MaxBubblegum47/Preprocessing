import os
import pickle
import PySimpleGUI as sg
from typing import Dict
sg.ChangeLookAndFeel('Black')
import string
from nltk.tokenize import word_tokenize
from itertools import chain
from glob import glob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import nltk
from nltk.stem import LancasterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

file = open("/Users/lorenzostigliano/Desktop/teststem/Paradise_Coldplay.txt","r") #put here the path of your song for testing the remove stopword functionality
righe = file.read()
words = righe.split()

#that's some bullshit test
lemmatizer = WordNetLemmatizer()
ps = LancasterStemmer()

#this is the right one that we're gonna use for real
lmtzr = WordNetLemmatizer()

for parole in words:
    parola = lmtzr.lemmatize(parole,'v')
    appendFile = open('filteredtext.txt','a')
    appendFile.write(" "+str(parola))
    appendFile.close()

with open("/Users/lorenzostigliano/Desktop/Progetto Gestione dell'Informazione/filteredtext.txt", "r") as f:
    with open("/Users/lorenzostigliano/Desktop/teststem/Paradise_Coldplay.txt", "w") as f1:
        for line in f:
            f1.write(line)

import os
os.remove("/Users/lorenzostigliano/Desktop/Progetto Gestione dell'Informazione/filteredtext.txt")
