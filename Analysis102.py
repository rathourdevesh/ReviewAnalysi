import pandas as pd

messages=pd.read_csv('E:/projects/iphoneReview/FilteredData5.csv', encoding = "utf-8",sep=",", names=["message","label"])
messages = messages.dropna(axis = 0, how ='any')
#messages = messages.dropna()

import re #regular Expression Library Import
import nltk #natural language toolkit Library Import
#nltk.download('stopwords')
#nltk.download('wordnet')
from nltk.corpus import stopwords # importing stopwords
import string

from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
ps = PorterStemmer()
wordnet = WordNetLemmatizer()

corpus = []
#
#creating the corpus
for i in range (0,len(messages)):
    if str(messages['message'][i]).strip() != 'nan':
        review = re.sub('[^a-zA-Z]',' ',messages['message'][i]) 
        review = review.lower()
        review = review.split()
        # review = [ps.stem(word) for word in review if not word in stopwords.words('english')] # removing stopwords
        review = [wordnet.lemmatize(word) for word in review if not word in stopwords.words('english')] # removing stopwords
        review = ' '.join(review)
        #print(review)
        corpus.append(review)
    

print(review)
print(messages['message'][len(messages)-1])
#print ('\n',corpus)
print(len(corpus))

# applying vectorization by bag of words model
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
#print(y)
print('\n -------------------------------------------')

#training the predictor

from sklearn.naive_bayes import MultinomialNB
sentiment_detect_model = MultinomialNB().fit(X_train,y_train)


y_pred = sentiment_detect_model.predict(X_test)


from sklearn.metrics import confusion_matrix,accuracy_score

confusion_m = confusion_matrix(y_test,y_pred)

accuracy =accuracy_score(y_test,y_pred)


print(confusion_m)

print('\n -------------------------------------------')

print('\n\n Accuracy = ',accuracy)



# doc = ['Phone is good good good good excellent ','Phone is excellent','Phone is too bad bad bad bad bad','phone is miserable','This is ba d idea','good ','excellent','too bad',' miserable','disapointing',
# 'too good ','Phone is excellent','Phone is too bad','phone is miserable','This is bad idea']
corpus2 = []
doc = pd.read_csv('E:/projects/iphoneReview/FilteredData4.csv',sep=",", names=["message2","label2"])
for i in range (0,len(doc)):
    review2= re.sub('[^a-zA-Z]',' ',doc['message2'][i])
    review2 = review2.lower()
    review2 = review2.split()
    review2 = [ps.stem(word) for word in review2 if not word in stopwords.words('english')] # removing stopwords
    review2 = ' '.join(review2)
    corpus2.append(review2)
X_new = cv.transform(corpus2) # this transforms the shape on the basis of mean and standard deviation derieved from the training model
print(X_new)
# k=[1,1,0,0,0,1,1,0,0,0,1,1,0,0,0]
y_check= pd.get_dummies(doc['label2'])
y_check=y_check.iloc[:,1].values
y_pred_new = sentiment_detect_model.predict(X_new)
print(y_pred_new)
accuracy2 =accuracy_score(y_check,y_pred_new)
print(accuracy2)


