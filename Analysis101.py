import pandas as pd

messages=pd.read_csv('E:/projects/iphoneReview/FilteredData2.csv',sep=",", names=["message","label"])


import re #regular Expression Library Import
import nltk #natural language toolkit Library Import
#nltk.download('stopwords')
from nltk.corpus import stopwords # importing stopwords

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

corpus = []


for i in range (0,len(messages)):
    review= re.sub('[^a-zA-Z]',' ',messages['message'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

print(review)
print(messages['message'][len(messages)-1])
print ('\n',corpus)
print(len(corpus))


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features= 5000)
X=cv.fit_transform(corpus).toarray()

y= pd.get_dummies(messages['label'])
y=y.iloc[:,1].values

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state = 0 )

print(X_train.shape,
        X_test.shape,
        y_train.shape,
        y_test.shape)
print(y)
print('\n -------------------------------------------')

from sklearn.naive_bayes import MultinomialNB
sentiment_detect_model = MultinomialNB().fit(X_train,y_train)


y_pred = sentiment_detect_model.predict(X_test)


from sklearn.metrics import confusion_matrix,accuracy_score

confusion_m = confusion_matrix(y_test,y_pred)

accuracy =accuracy_score(y_test,y_pred)


print(confusion_m)

print('\n -------------------------------------------')

print('\n\n Accuracy = ',accuracy)