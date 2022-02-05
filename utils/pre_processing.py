from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from spellchecker import SpellChecker
from string import punctuation
import contractions
import re


def remove_url(text):
    return re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", text)


def clean(text):
    text = remove_url(text)
    text = word_tokenize(text)
    text = [word.lower() for word in text]
    text = [word for word in text if word not in stopwords.words('english')]
    spell = SpellChecker()
    text = [spell.correction(word) for word in text]
    text = [contractions.fix(word) for word in text]
    text = ' '.join(text).split(' ')
    punctuation_cleaned = [symbol for symbol in punctuation if symbol not in '!#?']
    punctuation_cleaned = ''.join(punctuation_cleaned)
    text = [word for word in text if word not in punctuation_cleaned]
    print(text)
    return ' '.join(text)
