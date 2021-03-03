import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics

df = pd.read_csv('Natural Language Processing\\NLP Projects\\Text Classification\\moviereviews.tsv', sep='\t')
# removing the NaN values
df.dropna(inplace=True)

# detecting empty strings
blanks = []

for index,label,review in df.itertuples():
    if type(review)==str:
        if review.isspace():
            blanks.append(index)

# removing empty strings from dataset
df.drop(blanks, inplace=True)

# splitting data into train & test sets
X = df['review']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.33)

#function to print out the scores of the pipelines
def print_scores(y_test, predictions):
    
    #printing confusion matrix
    print('Confusion Matrix'.center(30,'-'))
    print(metrics.confusion_matrix(y_test,predictions))
    
    #printing classification report
    print('Classification Report'.center(30,'-'))
    print(metrics.classification_report(y_test,predictions))
    
    #printing accuracy score
    print('Accuracy Score: ',metrics.accuracy_score(y_test,predictions),'\n')


# building pipelines to vectorize the data, and comparing their scores
# ---- Naive Bayes pipeline ----
text_clf_nb = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')),('clf', MultinomialNB())])
text_clf_nb.fit(X_train, y_train)

# forming a prediction set
predictions_nb = text_clf_nb.predict(X_test)

# printing Naive Bayes scores
print('Naive Bayes pipeline'.center(55,'-'),'\n')
print_scores(y_test,predictions_nb)

# ----LinearSVC pipeline----
text_clf_lsvc = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')),('clf', LinearSVC())])
text_clf_lsvc.fit(X_train, y_train)

# forming a prediction set
predictions_lsvc = text_clf_lsvc.predict(X_test)

# printing out LSVC scores
print('LinearSVC pipeline'.center(55,'-'),'\n')
print_scores(y_test,predictions_lsvc)

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

# using sid to attach compound sores to dataset
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))
df['compound']  = df['scores'].apply(lambda score_dict: score_dict['compound'])
df['comp_score'] = df['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')

# printing out scores
print_scores(df['label'],df['comp_score'])

# testing out my own movie review
myreview = "A movie I really wanted to love was terrible. \
I'm sure the producers had the best intentions, but the execution was lacking."

print('Naive Bayes:',text_clf_nb.predict([myreview]))

print('LinearSVC:' ,text_clf_lsvc.predict([myreview]))

if sid.polarity_scores(myreview)['compound'] > 0:
    print('NLTK VADER: Positive')
elif sid.polarity_scores(myreview)['compound'] < 0:
    print('NLTK VADER: Negative')
else:
    print('Neutral')