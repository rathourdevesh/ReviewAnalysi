import pandas as pd

messages=pd.read_csv('E:/projects/iphoneReview/FilteredData5.csv', encoding = "utf-8",sep=",", names=["message","label"])
# messages = messages.dropna(axis = 0, how ='any')
messages = messages.dropna()
import re #regular Expression Library Import
import nltk #natural language toolkit Library Import
#nltk.download('stopwords')
from nltk.corpus import stopwords # importing stopwords
import string

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

corpus = []
# def remove_emoji(string):
#     emoji_pattern = re.compile("["
#                            u"\U0001F600-\U0001F64F"  # emoticons
#                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
#                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            u"\U00002702-\U000027B0"
#                            u"\U000024C2-\U0001F251"
#                            "]+", flags=re.UNICODE)
#     return emoji_pattern.sub(r'', string)
#creating the corpus
for i in range (0,len(messages)):
    #review = [messages['message'][i] for m in messages['message'][i] if m not in string.punctuation ]
    #review = remove_emoji(messages['message'][i])
    review = re.sub('[^a-zA-Z]',' ',messages['message'][i])
    #review = re.sub('[^a-zA-Z]',' ',review)
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')] # removing stopwords
    review = ' '.join(review)
    corpus.append(review)

print(review)
print(messages['message'][len(messages)-1])
print ('\n',corpus)
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
print(y)
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


