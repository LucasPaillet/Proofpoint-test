from csv import reader as csvReader
from datetime import datetime as dateTime
from pandas import DataFrame
from os import path as ospath

def getData(path: str) -> list[tuple[str, str, int]]:
    data = []
    with open(path, 'r', encoding='utf-8') as file:
        reader = csvReader(file)
        next(reader)
        for row in reader:
            title, author, year = row
            if not title:
                continue
            if not author:
                author = '--Author unknown--'
            try:
                year = int(year)
                if year < 0 or year > dateTime.now().year:
                    year = 0
            except:
                year = 0
            data.append((title, author, year))
    return data


def removeDuplicates(data: list[tuple[str, str, int]], columns: list[str]) -> DataFrame:
    frame = DataFrame(data, columns=columns)
    frame.drop_duplicates(inplace=True)
    return frame


def mainB(path: str, filter: int, columns: list[str]) -> DataFrame:
    data = getData(path)
    data = removeDuplicates(data, columns)
    filter = columns[filter]
    outputFile = ospath.join(ospath.dirname(__file__), f'booklist-by-{filter}.csv')
    data = data.sort_values(by=filter, ascending=True)
    data.to_csv(outputFile, sep=',', encoding='utf-8', index=False, header=True)
    return data