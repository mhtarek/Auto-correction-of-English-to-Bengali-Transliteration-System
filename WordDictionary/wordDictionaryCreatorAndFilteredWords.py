import csv

def removeDuplicateWords(dictionary):
   cleanDictionary = []
   for i in dictionary:
      if i not in cleanDictionary:
         cleanDictionary.append(i)
   return cleanDictionary

def filterWordDictionary(dictionary):
   for i in range(len(dictionary)):
      dictionary[i] = dictionary[i].replace(',','').replace('"','').replace('।','').replace('?','').replace('!','').replace(')','').replace('(','')

   #remove empty items created from spaces
   while '' in dictionary:
      dictionary.remove('')

   #remove duplicated items
   dictionary = removeDuplicateWords(dictionary)
   
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

def makeDictionaryFromBanglaDictionaryWords(filename):
    file = open(filename, 'r',encoding = 'utf-8')

    for line in file.readlines():
        fname = line.rstrip().split(',')
    #fname = filterWordDictionary(fname)
    fname.pop(0)

    return fname

def main():
   li = makeDictionaryFromBanglaDictionaryWords('corWords.txt')
   print(len(li))

