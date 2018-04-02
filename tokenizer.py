# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 22:48:59 2018

@author: NP
"""


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('train_E6oV3lV.csv')

# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

import nltk.tokenize import sent_tokenize ,word_tokenize

exp = 'i am fine Mr. jons. How about you? u didn\'t call me. is everything ok.'

print(sent_tokenize(exp)) 
