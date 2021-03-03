import pandas as pd 

#importing dataset
quora = pd.read_csv('Natural Language Processing\\NLP Projects\\Topic Modelling\\quora_questions.csv')

# data preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_df = 0.95, min_df=2, stop_words='english')

dtm = tfidf.fit_transform(quora['Question'])

# non-negative matrix factorization

from sklearn.decomposition import NMF

nmf_model = NMF(n_components=20)

nmf_model.fit(dtm)

# printing the top 20 most common words for each of the 20 topics
for index,topic in enumerate(nmf_model.components_):
    print(f'THE TOP 20 WORDS FOR TOPIC #{index}')
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-20:]])
    print('\n')

# adding a label to each topic
topic_label = {0:'Technology', 1:'Relationships', 2:'Q&A', 3:'Investing', 4:'Discussions', 5:'Politics', 6:'Programming', 7:'US Politics', 8:'Politics', 
9:'Work Culture', 10:'Engineering', 11:'India', 12:'Social Media', 13:'Communication', 14:'Health', 15:'Movies', 16:'Relationships',
17:'Technology', 18:'Software Engineering', 19:'Foreign'}

# adding a new column to the dataframe
topic_results = nmf_model.transform(dtm)

topic_results.argmax(axis=1)

quora['Topic'] = topic_results.argmax(axis=1)
quora['Label'] = quora['Topic'].map(topic_label)
quora.head()