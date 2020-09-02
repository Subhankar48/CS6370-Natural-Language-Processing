from util import *

from math import log2


class Evaluation():

    def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The precision value as a number between 0 and 1
        """
        number_of_docs_retrieved = len(query_doc_IDs_ordered)
        try:
            assert k <= number_of_docs_retrieved, "k greater than the number of documents retrived. Returning -1"
            num_true_docs_retrieved = 0
            for docID in query_doc_IDs_ordered[:k]:
                if int(docID) in true_doc_IDs:
                    num_true_docs_retrieved += 1
            precision = num_true_docs_retrieved/k
            return precision
        except AssertionError as message:
            print(message)
            return -1

    def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of precision of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean precision value as a number between 0 and 1
        """
        number_of_queries = len(query_ids)
        precisions = []
        try:
            assert len(doc_IDs_ordered) == len(
                query_ids), "Number of queries not equal to the number of sets of documents retrieved.\nReturning -1."
            for i in range(number_of_queries):
                query_doc_IDs_ordered = doc_IDs_ordered[i]
                query_id = int(query_ids[i])
                true_doc_IDs = []
                for dict_ in qrels:
                    if int(dict_["query_num"]) == int(query_id):
                        true_doc_IDs.append(int(dict_["id"]))
                precision = self.queryPrecision(
                    query_doc_IDs_ordered, query_id, true_doc_IDs, k)
                precisions.append(precision)
            try:
                assert len(precisions) != 0, "Error! Empty list. Returning -1."
                return sum(precisions)/len(precisions)
            except AssertionError as msg:
                print(msg)
                return -1

        except AssertionError as message:
            print(message)
            return -1

    def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The recall value as a number between 0 and 1
        """
        number_of_docs_retrieved = len(query_doc_IDs_ordered)
        number_of_true_docs = len(true_doc_IDs)
        try:
            assert k <= number_of_docs_retrieved, "k greater than the number of documents retrived. Returning -1"
            num_true_docs_retrieved = 0
            for docID in query_doc_IDs_ordered[:k]:
                if int(docID) in true_doc_IDs:
                    num_true_docs_retrieved += 1
            recall = num_true_docs_retrieved/number_of_true_docs
            return recall
        except AssertionError as message:
            print(message)
            return -1

    def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of recall of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean recall value as a number between 0 and 1
        """
        number_of_queries = len(query_ids)
        recalls = []
        try:
            assert len(doc_IDs_ordered) == len(
                query_ids), "Number of queries not equal to the number of sets of documents retrieved.\nReturning -1."
            for i in range(number_of_queries):
                query_doc_IDs_ordered = doc_IDs_ordered[i]
                query_id = query_ids[i]
                true_doc_IDs = []
                for dict_ in qrels:
                    if int(dict_["query_num"]) == int(query_id):
                        true_doc_IDs.append(int(dict_["id"]))

                recall = self.queryRecall(
                    query_doc_IDs_ordered, query_id, true_doc_IDs, k)
                recalls.append(recall)
            try:
                assert len(recalls) != 0, "Error! Empty list. Returning -1."
                return sum(recalls)/len(recalls)
            except AssertionError as msg:
                print(msg)
                return -1

        except AssertionError as message:
            print(message)
            return -1

    def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of IDs of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The fscore value as a number between 0 and 1
        """
        fscore = 0
        precision = self.queryPrecision(
            query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        recall = self.queryRecall(
            query_doc_IDs_ordered, query_id, true_doc_IDs, k)
        if (precision > 0 and recall > 0):
            fscore = 2*precision*recall/(precision+recall)
        return fscore

    def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of fscore of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean fscore value as a number between 0 and 1
        """

        number_of_queries = len(query_ids)
        fscores = []
        try:
            assert len(doc_IDs_ordered) == len(
                query_ids), "Number of queries not equal to the number of sets of documents retrieved.\nReturning -1."
            for i in range(number_of_queries):
                query_doc_IDs_ordered = doc_IDs_ordered[i]
                query_id = query_ids[i]
                true_doc_IDs = []
                for dict_ in qrels:
                    if int(dict_["query_num"]) == int(query_id):
                        true_doc_IDs.append(int(dict_["id"]))
                fscore = self.queryFscore(
                    query_doc_IDs_ordered, query_id, true_doc_IDs, k)
                fscores.append(fscore)
            try:
                assert len(fscores) != 0, "Error! Empty list. Returning -1."
                return sum(fscores)/len(fscores)
            except AssertionError as msg:
                print(msg)
                return -1

        except AssertionError as message:
            print(message)
            return -1

    def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of nDCG of the Information Retrieval System
        at given value of k for a single query

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The qrels list of dictionaries 
        arg4 : int
                The k value

        Returns
        -------
        float
                The nDCG value as a number between 0 and 1
        """
        number_of_docs_retrieved = len(query_doc_IDs_ordered)
        try:
            assert k <= number_of_docs_retrieved, "k greater than the number of documents retrived. Returning -1"
            relevance_vals = {}
            relevant_docs = []
            DCGk = 0
            IDCGk = 0
            for dict_ in true_doc_IDs:
                if int(dict_["query_num"]) == int(query_id):
                    id_ = int(dict_["id"])
                    relevance = 5-dict_["position"]
                    relevant_docs.append(int(id_))
                    relevance_vals[int(id_)] = relevance

            for i in range(1, k+1):
                docID = int(query_doc_IDs_ordered[i-1])
                if docID in relevant_docs:
                    relevance = relevance_vals[docID]
                    DCGk += (2**relevance-1)/log2(i+1)

            optimal_order = sorted(relevance_vals.values(), reverse=True)
            number_of_relevant_docs = len(optimal_order)
            for i in range(1, min(number_of_relevant_docs, k)+1):
                relevance = optimal_order[i-1]
                IDCGk += (2**relevance-1)/log2(i+1)

            try:
                assert IDCGk != 0, "IDCGk is zero. Returning -1"
                nDCGk = DCGk/IDCGk

                return nDCGk
            except AssertionError as msg:
                print(msg)
                return -1

        except AssertionError as message:
            print(message)
            return -1

    def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of nDCG of the Information Retrieval System
        at a given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries for which the documents are ordered
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The mean nDCG value as a number between 0 and 1
        """

        number_of_queries = len(query_ids)
        nDCGs = []
        try:
            assert len(doc_IDs_ordered) == len(
                query_ids), "Number of queries not equal to the number of sets of documents retrieved.\nReturning -1."
            for i in range(number_of_queries):
                query_doc_IDs_ordered = doc_IDs_ordered[i]
                query_id = int(query_ids[i])
                nDCG = self.queryNDCG(
                    query_doc_IDs_ordered, query_id, qrels, k)
                nDCGs.append(nDCG)
            try:
                assert len(nDCGs) != 0, "Error! Empty list. Returning -1."
                return sum(nDCGs)/len(nDCGs)
            except AssertionError as msg:
                print(msg)
                return -1

        except AssertionError as message:
            print(message)
            return -1

    def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
        """
        Computation of average precision of the Information Retrieval System
        at a given value of k for a single query (the average of precision@i
        values for i such that the ith document is truly relevant)

        Parameters
        ----------
        arg1 : list
                A list of integers denoting the IDs of documents in
                their predicted order of relevance to a query
        arg2 : int
                The ID of the query in question
        arg3 : list
                The list of documents relevant to the query (ground truth)
        arg4 : int
                The k value

        Returns
        -------
        float
                The average precision value as a number between 0 and 1
        """
        number_of_true_docs = len(true_doc_IDs)
        number_of_docs_retrieved = len(query_doc_IDs_ordered)
        try:
            assert k <= number_of_docs_retrieved, "k greater than the number of documents retrived. Returning -1"
            relevances = []
            precisions = []
            for docID in query_doc_IDs_ordered:
                if int(docID) in true_doc_IDs:
                    relevances.append(1)
                else:
                    relevances.append(0)
            for i in range(1, k+1):
                precision_at_i = self.queryPrecision(
                    query_doc_IDs_ordered, query_id, true_doc_IDs, i)
                precisions.append(precision_at_i)

            precision_at_k_times_rel_k = []
            for i in range(k):
                value = precisions[i]*relevances[i]
                precision_at_k_times_rel_k.append(value)

            try:
                assert number_of_true_docs != 0, "Number of true docs = 0. Returning -1."
                AveP = sum(precision_at_k_times_rel_k)/number_of_true_docs

                return AveP
            except AssertionError as msg:
                print(msg)
                return -1

        except AssertionError as message:
            print(message)
            return -1

    def meanAveragePrecision(self, doc_IDs_ordered, query_ids, qrels, k):
        """
        Computation of MAP of the Information Retrieval System
        at given value of k, averaged over all the queries

        Parameters
        ----------
        arg1 : list
                A list of lists of integers where the ith sub-list is a list of IDs
                of documents in their predicted order of relevance to the ith query
        arg2 : list
                A list of IDs of the queries
        arg3 : list
                A list of dictionaries containing document-relevance
                judgements - Refer cran_qrels.json for the structure of each
                dictionary
        arg4 : int
                The k value

        Returns
        -------
        float
                The MAP value as a number between 0 and 1
        """
        number_of_queries = len(query_ids)
        AvePs = []
        try:
            assert len(doc_IDs_ordered) == len(
                query_ids), "Number of queries not equal to the number of sets of documents retrieved.\nReturning -1."
            for i in range(number_of_queries):
                query_doc_IDs_ordered = doc_IDs_ordered[i]
                query_id = int(query_ids[i])
                true_doc_IDs = []
                for dict_ in qrels:
                    if int(dict_["query_num"]) == int(query_id):
                        true_doc_IDs.append(int(dict_["id"]))
                AveP = self.queryAveragePrecision(
                    query_doc_IDs_ordered, query_id, true_doc_IDs, k)
                AvePs.append(AveP)
            try:
                assert len(AvePs) != 0, "Error! Empty list. Returning -1."
                return sum(AvePs)/len(AvePs)
            except AssertionError as msg:
                print(msg)
                return -1

        except AssertionError as message:
            print(message)
            return -1
