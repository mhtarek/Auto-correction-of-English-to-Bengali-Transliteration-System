import csv


def filterWordDictionary(dictionary):
   for i in range(len(dictionary)):
      dictionary[i] = dictionary[i].replace(',','').replace('"','').replace('।','').replace('?','').replace('!','').replace(')','').replace('(','')

   #remove empty items created from spaces
   while '' in dictionary:
      dictionary.remove('')

   return dictionary
    
def makeDictionary(file):
   sentenceList = []
   with open(file, 'rU',encoding='utf-8') as infile:
       reader = csv.reader(infile)
       sentenceList = [i[0] for i in reader]
   sentenceList.pop(0)
   
   
   dictionaryList = []
   for element in sentenceList:
         dictionaryList.extend(element.split(' '))
         
   dictionaryList = filterWordDictionary(dictionaryList)

   return (dictionaryList)


def main():
   li = makeDictionary('../files/data.csv')
   print(len(li))

