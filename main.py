#import xml.etree.ElementTree as ET
#file_name="data\\1.xml"
#dom=ET.parse(file_name)
#root = dom.getroot()
#print(root.text)
from pandas import read_csv
import numpy as np
df = read_csv('train.csv',delimiter=",")
d=np.asarray(df)
print(d[0])
import sklearn.
import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC(gamma='auto')
clf.fit(X, y)




print(clf.predict([[2.1, 2]]))