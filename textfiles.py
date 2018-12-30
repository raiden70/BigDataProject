from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from pandas import read_csv
from XMLPARSER import XMLParser
t=XMLParser("data")
t=t.parseList()
tfidf=TfidfVectorizer(min_df=2,max_df=0.5,ngram_range=(1,1),lowercase=False)
features=tfidf.fit_transform(t)
d=pd.DataFrame(features.todense(),columns=tfidf.get_feature_names())
print(d)
s=np.asarray(d)
print(s[1])