from util import *
from collections import Counter
import math
import numpy as np


class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.docIDs = None

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = {}

		#Fill in code here
		for doc in docs:
			docID = docIDs[docs.index(doc)]
			terms = [term for sentence in doc for term in sentence] # Flattening 2d list to 1d
			for term, tf in list(Counter(terms).items()):
				try:
					index[term].append([docID, tf])
				except:
					index[term] = [[docID,tf]]

		self.docIDs = docIDs			
		self.index = index


	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		# Fill in code here

		index = self.index
		docIDs = self.docIDs

		# Getting idf for each term
		idf = {}
		nullvector = {}
		N = len(docIDs)
		for term in index:
			n = len(index[term])
			idf[term] = math.log10(float(N/n))
			nullvector[term] = 0

		# Representing documents in tf-idf vector space
		docvectors = {}
		for docID in docIDs:
			docvectors[docID] = nullvector.copy() # Initializing all docvectors with nullvector

		for term in index:
			for docID, tf in index[term]:
				docvectors[docID][term] = tf * idf[term]

		# Representing queries in tf-idf vector space and ranking documents based on cosine similarity
		for query in queries:
			queryvector = nullvector.copy()
			terms = [term for sentence in query for term in sentence] # Flattening 2d list to 1d
			for term, tf in list(Counter(terms).items()):
				try:
					queryvector[term] = tf * idf[term]
				except:
					pass

			cosinesimilarities = {}
			for docID in docIDs:
				try:
					cosinesimilarities[docID] = sum(docvectors[docID][key] * queryvector[key] for key in index) / (math.sqrt(sum(docvectors[docID][key] * docvectors[docID][key] for key in index)) * math.sqrt(sum(queryvector[key] * queryvector[key] for key in index)))
				except:
					cosinesimilarities[docID] = 0
			doc_IDs_ordered.append([docID for docID, tf in sorted(cosinesimilarities.items(), key=lambda item: item[1], reverse = True)])

		return doc_IDs_ordered