# -*- coding: utf-8 -*-
"""Fake news project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hDICCtNbY4RSm75RLPtNl6DZ1q4VnwZR

About the dataset:
1. id: unique id for a news article 
2. title: the title of news article 
3. author: author of the article 
4. text: the text of the article ; could be incomplete 
5. label: a label that marks whether the news article is real or fake 


    1: fake news
    0: real news
"""

import numpy as np
import pandas as pd 
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk
nltk.download('stopwords')

# printing the stop words in english
print(stopwords.words('english'))

"""Data preprocessing 

"""

path = '/content/drive/MyDrive/fake news ml project/train.csv'

news_dataset = pd.read_csv(path)

news_dataset.shape

# print first 5 rows of the dataframe
news_dataset.head()

# count the number of missing values in the dataset
news_dataset.isnull().sum()

# replacing the null values with empty string 
news_dataset = news_dataset.fillna('')

# merging the author name and news titles 
news_dataset['content'] = news_dataset['author']+' '+news_dataset['title']

print(news_dataset['content'])

# separating the data and label 
X = news_dataset.drop(columns = 'label',axis=1)
Y = news_dataset['label']

print(X)
print(Y)

"""Stemming :

stemming is the process of reducing a word to its Root word
"""

port_stem = PorterStemmer()

def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

news_dataset['content'] = news_dataset['content'].apply(stemming)

print(news_dataset['content'])

#separating the data and label
X = news_dataset['content'].values
Y = news_dataset['label'].values

print(X)

print(Y)

Y.shape

# converting the textual data to numerical data
vectorizer = TfidfVectorizer()
vectorizer.fit(X)

X = vectorizer.transform(X)

print(X)

"""Splitting the dataset to training & test data """

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)

"""training the model: Logisitc Regression """

model = LogisticRegression()

model.fit(X_train , Y_train)

"""Evaluation

accuracy score
"""

# accuracy score on the training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction , Y_train)

print('Accuracy score of the trainig data: ' , training_data_accuracy)

# accuracy score on the test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score of the test data: ' , test_data_accuracy)

"""Making a predictive System"""

X_new = X_test[3]

prediction = model.predict(X_new)
print(prediction)

if (prediction[0]==0):
  print('The news is real')
else:
  print('The news is fake')

print(Y_test[3])

