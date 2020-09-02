from util import *

# Add your import statements here
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

class StopwordRemoval():

    def fromList(self, text):
        """
        Sentence Segmentation using the Punkt Tokenizer

        Parameters
        ----------
        arg1 : list
                A list of lists where each sub-list is a sequence of tokens
                representing a sentence

        Returns
        -------
        list
                A list of lists where each sub-list is a sequence of tokens
                representing a sentence with stopwords removed
        """
        for sentence_number in range(len(text)):
                tokens_without_stop_words = []
                # create an empty list for each tokenized sentence
                list_of_tokens = text[sentence_number]
                for word in list_of_tokens:
                        if word not in stop_words:
                                tokens_without_stop_words.append(word)
                                # for each word in list of tokens:
                                        # If word is not found in stop words:
                                                # append that word to the list 'tokens_without_stop_words'
                text[sentence_number] = tokens_without_stop_words
                # Replace the corresponding tokenized sentence with 'tokens_without_stop_words'
        return text
