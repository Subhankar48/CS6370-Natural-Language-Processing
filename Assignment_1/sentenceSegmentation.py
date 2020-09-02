from util import *
# Add your import statements here
from nltk.tokenize import PunktSentenceTokenizer
import re


class SentenceSegmentation():

    def naive(self, text):
        """
        Sentence Segmentation using a Naive Approach

        Parameters
        ----------
        arg1 : str
                A string (a bunch of sentences)

        Returns
        -------
        list
                A list of strings where each string is a single sentence
        """
        if isinstance(text, str):
            # split the sentence using the delimiters
            segmentedText = re.split(delimiters, text)
            if '' in segmentedText:
                segmentedText.remove('')
            # remove unwanted empty characters
        else:
            print("Warning. Incorrect argument.")
            print("Returning zero.")
            return 0
        return segmentedText

    def punkt(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : str
                A string (a bunch of sentences)

        Returns
        -------
        list
                A list of strings where each strin is a single sentence
        """
        if (isinstance(text, str)):
            sentence_tokenizer = PunktSentenceTokenizer(text)
        #   create a PunktSentenceTokenizer object and tokenize using it
            segmentedText = sentence_tokenizer.tokenize(text)
            return segmentedText
        else:
            print('Warning. Argument passed not a string.')
            print('Zero returned')
            return 0
