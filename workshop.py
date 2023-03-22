import json
import os
os.getcwd()
data = open("sample.json",'r')
data = data.read()
# print(data)

data = json.loads(data)
# print(type(data))

glossary = data['glossary']
# print(glossary['title'])
# print(glossary['GlossDiv'])

glossdiv = glossary['GlossDiv']
print(glossdiv['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][0])