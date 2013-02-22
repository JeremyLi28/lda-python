#!/usr/bin/env python
#
# Gibbs Sampling for LDA

class Sampler(object):
	"""Sampler"""
	def __init__(self, alpha, beta):
		self.__alpha = alpha
		self.__beta = beta
		self.__document_topic_count = [[0]*num_topics for i in range(num_documents)]
		self.__document_topic_sum = [0]*num_documents
		self.__topic_word_count = [[0]*num_words for i in range(num_topics)]
		self.__topic_word_sum = [0]*num_topics

	def init_model_given_corpus(self, corpus, model):
		pass
		# init topic, term distribution
		for m in range(len(corpus)):
			document = corpus[m]
			iter = Document.Iterator(document)
			while not iter.done():
				print iter.word()
				print iter.topics()
				iter.next()

	def sample_loop(self, model):
		pass