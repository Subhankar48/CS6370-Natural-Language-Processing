from nltk.stem.snowball import SnowballStemmer
from nltk import pos_tag
from util import *

# Add your import statements here

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
stemmer = SnowballStemmer("english")


class InflectionReduction:

    def reduce(self, text):
        """
        Stemming

        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list a sequence of tokens
                representing a sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of
                stemmed tokens representing a sentence
        """
        
        if isinstance(text, list):
            for sentence_number in range(len(text)):
                # for a list of tokens corresponding to a sentence
                for word_number in range(len(text[sentence_number])):
                    text[sentence_number][word_number] = stemmer.stem(
                        text[sentence_number][word_number])
                    # for word in the list of tokens:
                        # stem the word and replace the corresponding word in the input list
                    pass
            return text

        else:
            print("Warning.")
            print("Wrong input type. Zero returned.")
            return 0

    # Not used here but coded just in case needed in future
    def reduce_using_lemmatization(self, text):
        """
        Lemmatization
        Declared in case required later on.

        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list a sequence of tokens
                representing a sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of
                stemmed/lemmatized tokens representing a sentence
        """
        if isinstance(text, list):
            for sentence_number in range(len(text)):
                pos_tags = pos_tag(text[sentence_number])
                # find the pos_tag for each word in a sentence
                for word_number in range(len(text[sentence_number])):
                    # convert the pos_tag to a format recognizable by the wordnet lemmatizer
                    pos = convert_to_wordnet_understandable_POS(
                        pos_tags[word_number][1])
                    text[sentence_number][word_number] = wordnet_lemmatizer.lemmatize(
                        text[sentence_number][word_number], pos=pos)
            return text

        else:
            print("Warning.")
            print("Wrong input type. Zero returned.")
            return 0
