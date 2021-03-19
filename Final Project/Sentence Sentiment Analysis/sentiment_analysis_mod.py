#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 22:28:31 2021

@author: sagarlamsal
"""

import nltk
import random
import pickle
import io


##from nltk.corpus import movie_reviews
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.classify import ClassifierI

from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from statistics import mode



class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
        

documents_f = open("files_documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()




word_features_f = open("word_features.pickle", "rb")
word_features = pickle.load(word_features_f)
word_features_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features



featuresets_f = open("featuresets.pickle", "rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

random.shuffle(featuresets)
print(len(featuresets))



testing_set = featuresets[10000:]
training_set = featuresets[:10000]



open_file = open("naivebayestest.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()


open_file = open("MNB_pickled.pickle", "rb")
MNB_classifier = pickle.load(open_file)
open_file.close()



open_file = open("Bernoulli_pickled.pickle", "rb")
BB_classifier = pickle.load(open_file)
open_file.close()


open_file = open("LR_pickled.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()


# =============================================================================
# 
# open_file = open("SGDC_pickled.pickle.pickle", "rb")
# SGDC_classifier = pickle.load(open_file)
# open_file.close()
# 
# 
# =============================================================================
open_file = open("LSVC_pickled.pickle", "rb")
LinearSVC_classifier = pickle.load(open_file)
open_file.close()





voted_classifier = VoteClassifier(
                                  classifier,
                                  MNB_classifier,
                                  BB_classifier,
                                  LogisticRegression_classifier,
                                  #SGDC_classifier,
                                  LinearSVC_classifier,                                                                 
                                  )




def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)