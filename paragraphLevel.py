import csv
from fuzzywuzzy import fuzz

def removeDuplicateLines(sentenceList):
   cleansentenceList = []
   for i in sentenceList:
      if i not in cleansentenceList:
         cleansentenceList.append(i)
   return cleansentenceList

def Average(lst): 
    return sum(lst) / len(lst)
   
def multiSelection(sameWords,inputLine):
    inputLine  = inputLine.replace(" ", "")

    sentenceList = []
    with open('./files/data.csv', 'rU',encoding='utf-8') as infile:
    #with open('file.csv', 'rU',encoding='utf-8') as infile:
       reader = csv.reader(infile)
       sentenceList = [i[0] for i in reader]
    sentenceList.pop(0)

    for i in range(len(sentenceList)):
       sentenceList[i] = sentenceList[i].replace(" ", "")
    
    newList = []
    for j in range(len(sameWords)):
        for i in range(len(sentenceList)):
            if sameWords[j] in sentenceList[i]:
                newList.append(sentenceList[i])

    newList = removeDuplicateLines(newList)
    print(newList)

    dist1 = []
    for i in range(len(newList)):
        value = fuzz.token_set_ratio(newList[i],inputLine)
        dist1.append(value)
    print(dist1)
    

    avg_dist = []
    maxIndx = 0
    for j in range(len(sameWords)):
       dist = []
       count = 0
       for i in range(len(newList)):
          if sameWords[j] in newList[i]:
             count = count + 1
             value = fuzz.token_set_ratio(newList[i],inputLine)
             dist.append(value)
       if count==0:
          continue
       else:
          avg_dist.append(Average(dist))
          maxIndx = avg_dist.index(max(avg_dist))
       print(avg_dist)
    return sameWords[maxIndx]
   

def main():
   inputLine = 'কলম দিয়ে লিখতে হয়।'
   sameWordsList = ['লিখতে','বেলুন']

   selectedWord = multiSelection(sameWordsList,inputLine)

   print(selectedWord)

#main()
