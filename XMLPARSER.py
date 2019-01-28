import xml.etree.ElementTree as ET
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from os import listdir
from os.path import isfile, join
import pandas as pd
import shutil
class XMLParser:
    def __init__(self,path):
        self.directory=path
        self.file_names = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]
    def parse(self):
        stemmer = PorterStemmer()
        lemmatiser = WordNetLemmatizer()
        t=[]
        for i in range(0,len(self.file_names)):
            dom = ET.parse(self.directory+"\\"+self.file_names[i])
            root = dom.getroot()
            doc_word=str(root.text)
            token=word_tokenize(doc_word)
            clean_tokens=[]
            words = [word for word in token if word not in stopwords.words('english') and word.isalpha()]
            for word in words:
                clean_tokens.append(stemmer.stem(lemmatiser.lemmatize(word.lower())))
            s = ' '.join(clean_tokens)
            t.append(s)
        return t
    def move_tests_Files(self,testcsvfile):
        df = pd.read_csv('test.csv', delimiter=",")
        d = df['file']
        for i in d:
            shutil.move("data/" + i, "test_set/" + i)
            print(i)


