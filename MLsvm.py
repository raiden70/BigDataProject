import numpy as np
from  XMLPARSER import XMLParser
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from nltk.corpus import stopwords

#X = np.array([[1,1,10,12], [2,20,23,24], [3,100,102,112], [4,500,1000,1200]])
#y = np.array(["yacine", "yacine", "mokrani", "mokrani"])

#clf.fit(X, y)
#print(clf.predict([[2, 2,10,30]]))

#x=XMLParser("data").parseList()
#tfidf=TfidfVectorizer(min_df=2,max_df=0.5,ngram_range=(1,1),lowercase=False)
#features=tfidf.fit_transform(x)
#d=pd.DataFrame(features.todense(),columns=tfidf.get_feature_names())
#print(d)
# X_train=np.array(d[:4800])
# X_test=np.array(d[4800:5000])
# #print(X)
# #get Y
# df = pd.read_csv('train.csv',delimiter=",")
# Y=np.asarray(df[df.columns[-1]])
# clf = SVC(gamma='auto')
# clf.fit(X_train,Y)
# b = set(clf.predict(X_train))
# print(b)

#from sklearn.feature_extraction.text import CountVectorizer
#count_vect = CountVectorizer()
#X_train_counts = count_vect.fit_transform(x)
#print(X_train_counts.shape)

import os
import shutil

#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
df = pd.read_csv('test.csv',delimiter=",")
d=df['file']

for i in d:
    #os.rename("data/"+i, "test_set/"+i)
    shutil.move("data/"+i, "test_set/"+i)
    print(i)