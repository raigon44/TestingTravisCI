
# coding: utf-8

# In[80]:

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np


# In[56]:

train_set = fetch_20newsgroups(subset='train', shuffle=True)


# In[57]:

train_set.target


# In[58]:

print("\n".join(train_set.data[1].split("\n"))) #prints first line of the first data file


# In[59]:

#Bag of words

#Tockenizing
#Counting
#Normalizing

#each individual token occurrence frequency (normalized or not) is treated as a feature.
#the vector of all the token frequencies for a given document is considered a multivariate sample.

#A corpus of documents can thus be represented by a matrix with one row per document and one column per token
#occurring in the corpus.

#Documents are described by word occurrences while completely ignoring the relative position information
#of the words in the document


# In[ ]:




# In[60]:

#CountVectorizer does Tockenizing & Counting part

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train_set.data)
X_train_counts.shape


# In[61]:

X_train_counts


# In[62]:

count_vect.get_feature_names()


# In[63]:

print(count_vect.vocabulary_.get('crypt'))


# In[64]:

#TF-IDF

transform = TfidfTransformer()

Xtrain_tfidf = transform.fit_transform(X_train_counts)


# In[65]:

Xtrain_tfidf.shape


# In[66]:

#class conditional independence
#frequency table
#likelyhood table
#posterior probablity


#https://www.reddit.com/r/MachineLearning/comments/1inxnq/how_to_factor_in_tfidf_with_naive_bayes/
    


# In[67]:


clf = MultinomialNB().fit(Xtrain_tfidf, train_set.target)


# In[68]:

test_set = fetch_20newsgroups(subset='test', shuffle=True)


# In[70]:



Ytest = count_vect.transform(test_set.data)
Ytest_tfidf = transform.transform(Ytest)
predicted = clf.predict(Ytest_tfidf)
np.mean(predicted == test_set.target)


# In[74]:

#SVM classifier

svm_clf = SGDClassifier().fit(Xtrain_tfidf, train_set.target)



# In[75]:

predicted_svm = svm_clf.predict(Ytest_tfidf)
np.mean(predicted_svm == test_set.target)


# In[78]:

#Grid Search CV - to optimize parameters
#not working

'''parameters_svm = {'vect__ngram_range': [(1, 1), (1, 2)],
              'tfidf__use_idf': (True, False),
              'clf-svm__alpha': (1e-2, 1e-3),}

gs_clf_svm = GridSearchCV(svm_clf, parameters_svm, n_jobs=-1)

gs_clf_svm = gs_clf_svm.fit(Xtrain_tfidf, train_set.target)

gs_clf_svm.best_score_
gs_clf_svm.best_params_'''


# In[85]:

#Bernoulli Navie Bayes algorithm

BNclf = BernoulliNB(binarize=0.0).fit(Xtrain_tfidf, train_set.target)

predicted_BNB = BNclf.predict(Ytest_tfidf)
np.mean(predicted_BNB == test_set.target)



# In[79]:

#exp

from sklearn import datasets

iris = datasets.load_iris()

iris.data[0]

