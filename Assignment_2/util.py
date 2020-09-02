# Add your import statements here
from nltk.corpus import wordnet
# list of punctuations, delimiters and symbols used to separate words
punctuations = ['?', ':', '!', '.', ',', ';']
delimiters = '[.?!]'
word_separators = "[' ,-/]"

# convert the return variables of nltk.pos_tags
def convert_to_wordnet_understandable_POS(pos):
    if pos.startswith("J"):
        return wordnet.ADJ
    elif pos.startswith("V"):
        return wordnet.VERB
    elif (pos.startswith("N")) | (pos.startswith("P")):
        return wordnet.NOUN
    elif pos.startswith("R"):
        return wordnet.ADV
    else:
        # If none of the types match, classify it as a noun
        return wordnet.NOUN
threshold = 0.1
# Add any utility functions here
