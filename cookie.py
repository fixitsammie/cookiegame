"""program that solves the cookie game and gives a list of words"""
import itertools
import json
import os, sys

def load_words():
    try:
        filename ="words_dictionary.json"
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)
letters="shfle"
n_letter_word=3
n=n_letter_word
english_words = load_words()
combo=itertools.permutations(letters,n)
jombo=["".join(i) for i in combo]

for i in jombo:
    try:
        english_words[i.lower()]
        nu=1
    except:
        nu=0
    if nu==1:
        print(i.lower())
    nu=0
