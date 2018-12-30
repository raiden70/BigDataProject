#import xml.etree.ElementTree as ET
#file_name="data\\1.xml"
#dom=ET.parse(file_name)
#root = dom.getroot()
#print(root.text)
import pandas as pd
from pandas import read_csv
import numpy as np
df = read_csv('train.csv',delimiter=",")
d=np.asarray(df)
print(d[0])
from sklearn.feature_extraction.text import TfidfVectorizer
text=["good","not good","evil and good","more evil","makok","yaya","not","not nono not not not","not","not","not","not not not"]


from XMLPARSER import XMLParser
t=XMLParser("data")
print(t.parseList())
tfidf=TfidfVectorizer(min_df=2,max_df=0.5,ngram_range=(1,2))
features=tfidf.fit_transform(text)
d=pd.DataFrame(features.todense(),columns=tfidf.get_feature_names())
print(d)




import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC(gamma='auto')
clf.fit(X, y)




print(clf.predict([[2.1, 2]]))