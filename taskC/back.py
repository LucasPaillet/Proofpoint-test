from pandas import DataFrame
from string import punctuation
from re import sub
from unicodedata import normalize, combining
from os import path as ospath


def removeAcents(text: str) -> str:
    text = normalize('NFKD', text)
    return ''.join([char for char in text if not combining(char)])


def getWordsList(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as file:
        wordsList = (sub(f'[{punctuation}]','', removeAcents(file.read()))).split()
        pos = 0
        end = len(wordsList)
        while pos < end:
            wordsList[pos] = wordsList[pos].lower()
            pos += 1
        return wordsList


def countWords(wordsList: list[str]) -> dict:
    wordCounter = {}
    for word in wordsList:
        if word in wordCounter.keys():
            wordCounter[word] += 1
        else:
            wordCounter[word] = 1
    return wordCounter


def presentation(wordCounter: dict, columns: list[str]) -> DataFrame:
    data = [(key, value) for key, value in wordCounter.items()]
    frame = DataFrame(data, columns=columns).sort_values('Count', ascending=False)
    return frame[0:10]


def mainC(path:str, columns: list[str]) -> DataFrame:
    wordsList = getWordsList(path)
    wordsDict = countWords(wordsList)
    outputFile = ospath.join(ospath.dirname(__file__), 'wordCounter.csv')
    data = presentation(wordsDict, columns)
    data.to_csv(outputFile, sep=',', encoding='utf-8', index=False, header=True)
    return data