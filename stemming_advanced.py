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

list_file=[]
list_file = [(root, files) for root, dirs, files in os.walk("/home/lorenzo/Scrivania/Progetto Gestione dell'Informazione/Lyrics") if files]
list_file.sort()


for path, files in list_file:
    print(path)
    for canzoni in files:
        file = open(path +"/" + str(canzoni),"r")
        print(canzoni)
        righe = file.read()
        words = righe.split()
        lemmatizer = WordNetLemmatizer()
        ps = LancasterStemmer()

        lmtzr = WordNetLemmatizer()

        for parole in words:
            parola = lmtzr.lemmatize(parole,"v")
            appendFile = open("/home/lorenzo/Scrivania/Progetto Gestione dell'Informazione/Search Engine/filteredtext.txt","a")
            appendFile.write(" "+str(parola))
            appendFile.close()

        with open("/home/lorenzo/Scrivania/Progetto Gestione dell'Informazione/Search Engine/filteredtext.txt", "r") as f:
            with open(path +"/" + str(canzoni), "w") as f1:
                for line in f:
                    f1.write(line)

        import os
        try:
            myfile = "/home/lorenzo/Scrivania/Progetto Gestione dell'Informazione/Search Engine/filteredtext.txt"
            with open(myfile, "w") as f:
                f.write(" ")
        except FileNotFoundError()():
            print("File filteredtext NOT found")
