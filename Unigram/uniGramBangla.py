import nltk, re, string, collections
from nltk.util import ngrams
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

def createUnigram(file):
    dictinary = makeDictionary(file)
    unigram = ngrams(dictinary, 1)

    unigramFreq = collections.Counter(unigram)
    
    return unigramFreq


def findMax(wordList,uniGram):
    maxVal = -10
    word = ''
    for k,v in uniGram.items():
        
        for i in range(len(wordList)):
            if wordList[i] in k:    
                if maxVal < v:
                    maxVal = v
                    word = wordList[i]
    if word == '':
        print('not Found')
        word = wordList[0]
        
    return word

def printUniGram(uniGram):
    for k,v in uniGram.items():
        print(k,'-----',v)
        
def sortByMostCommon(unigram):
   counts = collections.Counter(unigram)
   x = counts.most_common()
   for k,v in x:
        print(k,'-----',v)
   
def main():
    myUniGram = createUnigram('../files/data.csv')
    print(len(myUniGram))
    #sortByMostCommon(myUniGram)
    wordList = ['করি','সে','করেছ','আমার' ]

    #word = findMax(wordList,myUniGram)
    #print(word)



#main()










