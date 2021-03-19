#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:03:21 2021

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
        
    
    
# =============================================================================
# 
# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
# 
# 
# 
# # =============================================================================
# # for category in movie_reviews.categories():
# #     for fileid in movie_reviews.fileids(category):
# #         documents.append(list(movie_reviews.words(fileid)), category)
# # 
# # =============================================================================
# 
# 
# #random.shuffle(documents)
# 
# #print(documents[1])
# =============================================================================

# =============================================================================
# 
# io.open('positive.txt', encoding='latin-1')
# io.open('negative.txt', encoding='latin-1')
# =============================================================================
    
    
    
    
    
short_pos = io.open("positive.txt", "r", encoding = 'latin-1').read()

short_neg = io.open("negative.txt", "r", encoding = 'latin-1').read()

documents = []

for r in short_pos.split('\n'):
    documents.append( (r, "pos") )

for r in short_neg.split('\n'):
    documents.append( (r, "neg") )


all_words = []

short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
    all_words.append(w.lower())

for w in short_neg_words:
    all_words.append(w.lower())
    

# =============================================================================
# 
# for w in movie_reviews.words():
#     all_words.append(w.lower())
# =============================================================================



# =============================================================================
# print(all_words.most_common(15))
# print(all_words['stupid'])
# 
# =============================================================================



#  j is adject, r is adverb, and v is verb
#allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]

for p in short_pos.split('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

    
for p in short_neg.split('\n'):
    documents.append( (p, "neg") )
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())


save_documents = open("files_documents.pickle",'wb')
pickle.dump(documents, save_documents)
save_documents.close()



all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]


save_features = open("word_features.pickle","wb")
pickle.dump(word_features, save_features)
save_features.close()




def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

#print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]

save_featuresets = open("featuresets.pickle","wb")
pickle.dump(featuresets, save_featuresets)
save_featuresets.close()

random.shuffle(featuresets)

# positive data example:      
training_set = featuresets[:10000]
testing_set =  featuresets[10000:]

##
### negative data example:      
##training_set = featuresets[100:]
##testing_set =  featuresets[:100]


# posterior = prior occurences x liklihood/evidence

classifier = nltk.NaiveBayesClassifier.train(training_set)

print(" Original Naive Bayes accuracy: ", (nltk.classify.accuracy(classifier, testing_set))*100)

classifier.show_most_informative_features(15)


# Save Classifier with Pickle


classifier_f = open('naivebayestest.pickle', 'rb')
classifier = pickle.load(classifier_f)
classifier_f.close()



# =============================================================================
# save_classifier = open("naivebayestest.pickle", "wb")  #wb = write in bytes
# pickle.dump(classifier, save_classifier)
# save_classifier.close()
# 
# =============================================================================




#SciKit bayes

#Multinomial Bayes
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print(" MNB_classifier Bayes accuracy: ", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)


save_classifier = open("MNB_pickled.pickle",'wb')
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()





# Gaussian Bayes
# =============================================================================
# GB_classifier = SklearnClassifier(GaussianNB())
# GB_classifier.train(training_set)
# print(" GB_classifier Bayes accuracy: ", (nltk.classify.accuracy(GB_classifier, testing_set))*100)
# 
# =============================================================================





# Bernoulli Bayes
BB_classifier = SklearnClassifier(BernoulliNB())
BB_classifier.train(training_set)
print(" Bernoulli_classifier accuracy: ", (nltk.classify.accuracy(BB_classifier, testing_set))*100)


save_classifier = open("Bernoulli_pickled.pickle", 'wb')
pickle.dump(BB_classifier, save_classifier)
save_classifier.close()

# =============================================================================
# # LogisticRegression, SGDClassifier
# # SVC, LinearSVC, NuSVC
# 
# =============================================================================


LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print(" LogisticRegression Bayes accuracy: ", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("LR_pickled.pickle",'wb')
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()



SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print(" SGDClassifier_classifier Bayes accuracy: ", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

save_classifier = open("SGDC_pickled.pickle","wb")
pickle.dump(SGDClassifier_classifier, save_classifier)
save_classifier.close()





##SVC_classifier = SklearnClassifier(SVC())
##SVC_classifier.train(training_set)
##print("SVC_classifier accuracy percent:", (nltk.classify.accuracy(SVC_classifier, testing_set))*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)


save_classifier = open("LSVC_pickled.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()




# =============================================================================
# 
# NuSVC_classifier = SklearnClassifier(NuSVC())
# NuSVC_classifier.train(training_set)
# print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)
# 
# save_classifier = open("NuSVC_pickled.pickle","wb")
# pickle.dump(NuSVC_classifier, save_classifier)
# save_classifier.close()
# 
# =============================================================================

#combining and voting
voted_classifier = VoteClassifier(classifier,                               
                                  MNB_classifier,
                                  BB_classifier,
                                  LogisticRegression_classifier,
                                  SGDClassifier_classifier,
                                  LinearSVC_classifier,
                                  )

print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)



# =============================================================================
# print("Classification: ", voted_classifier.classify(testing_set[0][0]), 
#       "Confidence %: ", voted_classifier.confidence(testing_set[0][0])*100)
# 
# 
# 
# print("Classification: ", voted_classifier.classify(testing_set[1][0]), 
#       "Confidence %: ", voted_classifier.confidence(testing_set[1][0])*100)
# 
# print("Classification: ", voted_classifier.classify(testing_set[2][0]), 
#       "Confidence %: ", voted_classifier.confidence(testing_set[2][0])*100)
# 
# print("Classification: ", voted_classifier.classify(testing_set[3][0]), 
#       "Confidence %: ", voted_classifier.confidence(testing_set[3][0])*100)
# 
# print("Classification: ", voted_classifier.classify(testing_set[4][0]), 
#       "Confidence %: ", voted_classifier.confidence(testing_set[4][0])*100)
# 
# print("Classification: ", voted_classifier.classify(testing_set[5][0]), 
#       "Confidence %: ", voted_classifier.confidence(testing_set[5][0])*100)
# 
# 
# =============================================================================
