from fuzzywuzzy import fuzz
import csv
from pyavrophonetic import avro
import WordDictionary.wordDictionaryCreatorAndFilteredWords as dictionary
import Unigram.uniGramBangla as unigram
from BanglaWordSort.bangla_sort import bangla
import re
from sklearn.metrics import accuracy_score
from paragraphLevel import multiSelection


#Globally Making a word dictionary
WordDictionary = dictionary.makeDictionary('./files/data.csv')
WordDictionary = sorted(WordDictionary, key=bangla)
#print(WordDictionary)


def correct(inputLine):
        string_words = inputLine.split()
        
        for i in range(len(string_words)):
            if is_number(string_words[i]):
                    continue
                
            suggestions = []
            value =[]
            for name in WordDictionary:
                if string_words[i] == name:
                    value.append(fuzz.ratio(string_words[i], name))
                    suggestions.append(name)
                elif fuzz.ratio(string_words[i], name) >= 65:
                    value.append(fuzz.ratio(string_words[i], name))
                    suggestions.append(name)
            print(suggestions)
            print(value)

            if len(suggestions) > 0:
                maxPer = 0
                cor = ''
                for name in suggestions:
                    percent = fuzz.ratio(string_words[i], name)
                    if percent > maxPer:
                        if checkSameSuggestion(value):
                                newList = wordWithMaxScore(value,suggestions)
                                cor = multiSelection(newList,inputLine)
                        else:
                                cor = name
                                
                        maxPer = percent

                            
                print(cor,'---',maxPer,'\n')
                string_words[i] = cor
                
        return " ".join(string_words)

def wordWithMaxScore(value,string):
    
    valueLi = []
    newStr = []

    for i in range(len(value)):
        if max(value) == value[i]:
            valueLi.append(i)

    for i in range(len(valueLi)):
        newStr.append(string[valueLi[i]])

    return newStr

def is_number(s):
    try:
        float(s) 
    except ValueError:
        try:
            complex(s) 
        except ValueError:
            return False

    return True

def checkSameSuggestion(wordList):
    same = False
    count = 0
    for i in range(len(wordList)):
        if max(wordList) == wordList[i]:
            count+=1

            if count>1:
                same = True

    if same == True:
        return 1
    else:
         return 0
def createTestDataList(fileLocation):
        with open (fileLocation, "r",encoding = 'utf-8') as myfile:
            banglish_sentence=myfile.readlines()
        testData = banglish_sentence[0].split(' ')
        testData.pop(0)
        return testData

def checkFloat(string):
    string1 = string.split(" ")

    oldFloat = re.findall("[-|+]?\d+\।\d+", string)


    c = []
    for i in range(len(oldFloat)):
        for j in range(len(string1)):
            if oldFloat[i] == string1[j]:
                c.append(j)
    for i in range(len(oldFloat)):
        oldFloat[i] = oldFloat[i].replace('।','.')

    for i in range(len(oldFloat)):
        string1[c[i]] = oldFloat[i]

    return " ".join(string1)

def main():
    
    with open ("./True Value/test data/2.txt", "r",encoding = 'utf-8') as myfile:
            banglish_sentence=myfile.readlines()

    string_to_be_checked = checkFloat(avro.parse(banglish_sentence))
        
    prdicted_sentence = correct(string_to_be_checked)
    
    print("\nConverted sentence: ", string_to_be_checked,'\n')
    print(prdicted_sentence)

    trueTestData = createTestDataList("./True Value/true data/2True.txt")
    predictedData = prdicted_sentence.split(' ')

    
    print(trueTestData)
    print(predictedData)
    
    print("Total Number Of Test Word: ",len(predictedData))
    errorData = 0
    for i in range(len(predictedData)):
            if predictedData[i] == trueTestData[i]:
                    continue
            else:
                    errorData += 1
                    
    print("Corrected Word: ", len(predictedData) - errorData)
    print("Failed To Correct Word: ",errorData)
    
    accuracy = accuracy_score(trueTestData, predictedData)
    
    print("Accuracy: ",accuracy*100)
        
    
main()
