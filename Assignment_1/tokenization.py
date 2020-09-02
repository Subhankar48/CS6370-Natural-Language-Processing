from nltk.tokenize import TreebankWordTokenizer
from util import *
# Add your import statements here
import re

class Tokenization():

    def naive(self, text):
        """
        Tokenization using a Naive Approach

        Parameters
        ----------
        arg1 : list
                A list of strings where each string is a single sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of tokens
        """
        tokenizedText = []
        if isinstance(text, list):
            for sentence in text:
                if isinstance(sentence, str):
                    tokenizedText_ = re.split(word_separators, sentence)
                    # split the sentence at the word_separators using re library
                    for word in tokenizedText_:
                        if word in punctuations:
                            tokenizedText_.remove(word)
                        elif word ==' ':
                            tokenizedText_.remove(word)
                        elif word =='':
                            tokenizedText_.remove(word)
                        # remove the unwanted spaces and empty characters as well as punctuation symbols
                    tokenizedText.append(tokenizedText_)
                    # append tokenizedText_ to tokenizedText(which is to be returned)  
                else:
                    print("Warning")
                    print("Sentences are not in the form of strings")
                    return 0
        else:
            print("Warning")
            print("Argument not in the form of a list.")
            return 0
        return tokenizedText

    def pennTreeBank(self, text):
        """
        Tokenization using the Penn Tree Bank Tokenizer

        Parameters
        ----------
        arg1 : list
                A list of strings where each string is a single sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of tokens
        """
        tokenizedText = []
        if isinstance(text, list):
            for sentence in text:
                if isinstance(sentence, str):
                    tokenizedText_ = TreebankWordTokenizer().tokenize(sentence)
                    for word in tokenizedText_:
                        if word in punctuations:
                            # remove any unwanted punctuation symbols which have been calssified as tokens
                            # was not getting unwanted spaces with punkt so that part has been ignored
                            tokenizedText_.remove(word)
                    tokenizedText.append(tokenizedText_)
                else:
                    print("Warning")
                    print("Sentences are not in the form of strings")
                    return 0
        else:
            print("Warning")
            print("Argument not in the form of a list.")
            return 0
        return tokenizedText
