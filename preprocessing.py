#Lowercase
#togliere punteggiatura
#togliere whitespaces
#tokenizzare

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
nltk.download('stopwords')

list_file=[]
list_file = [(root, files) for root, dirs, files in os.walk("/Users/lorenzostigliano/Desktop/Lyrics") if files] #change the path with the one within you got all your .txt file
list_file.sort()



i=0
for path, files in list_file:
    for canzoni in files:
        try:
            stop_words = set(stopwords.words('english'))

            with open(path + "/" + canzoni, encoding = "ISO-8859-1") as f:
                line = f.read()
                print(line)

            words = line.split()
            for r in words:
                if not r in stop_words:
                    appendFile = open('filteredtext.txt','a')
                    appendFile.write(" "+str(r))
                    appendFile.close()

            with open("/Users/lorenzostigliano/Desktop/Progetto Gestione dell'Informazione/filteredtext.txt", "r") as f:
                with open(path + "/" + canzoni, "w") as f1:
                    for line in f:
                        f1.write(line)

            import os
            os.remove("/Users/lorenzostigliano/Desktop/Progetto Gestione dell'Informazione/filteredtext.txt")

            #LOWER CASE,PUNTEGGIATURA, LEMMATIZING, STEMMING
            #lines = [line.lower() for line in f] OK
            #lines = [re.sub("[\(\[].*?[\)\]]", '', line) for line in f] Rimuove tutta la roba tipo [verse1]
            #lines = [line.translate(str.maketrans('','',string.punctuation)) for line in f] rimuove la punteggiatura
            #lines= [word_tokenize(line) for line in f] #Tokenization OK


            f.close()

        except FileNotFoundError:
            i+=1

print("file non trovati: " + str(i))
