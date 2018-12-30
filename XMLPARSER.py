import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join
class XMLParser:
    def __init__(self,path):
        self.directory=path
        self.file_names = [f for f in listdir(self.directory) if isfile(join(self.directory, f))]

    def parse(self,filename):
        dom = ET.parse(filename)
        root = dom.getroot()
        print(root.text)