import sys
import os


def ConvertFileLink(CurrentFilePath):
    data = os
    base = data.path.dirname(sys.argv[0])
    name = data.path.normpath(data.path.join(base, CurrentFilePath))
    return name


def Read(CurrentFilePath):
    path = ConvertFileLink(CurrentFilePath)
    Files = open(path, "r", encoding="utf-8-sig")
    result = Files.read()
    Files.close()
    return result


def ReadCSV(CurrentFilePath):
    TextData = Read(CurrentFilePath)
    Result = []
    Array1 = TextData.split("\n")
    cnt = 0
    while cnt < len(Array1):
        Work = Array1[cnt].split(",")
        Result.append(Work)
        cnt = cnt + 1
    return Result


def Write(CurrentFilePath, WriteString, FileReadMode):
    path = ConvertFileLink(CurrentFilePath)
    Files = open(path, FileReadMode, encoding="UTF-8")
    Files.write(WriteString)
    Files.close()


def WriteAdd(CurrentFilePath, WriteString):
    Write(CurrentFilePath, WriteString, "a")


def WriteNew(CurrentFilePath, WriteString):
    Write(CurrentFilePath, WriteString, "w")


def Clear(CurrentFilePath):
    WriteNew(CurrentFilePath, "")
