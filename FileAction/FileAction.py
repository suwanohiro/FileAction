import sys
import os


def ConvertFileLink(CurrentFilePath):
    """
    相対パスを絶対パスに変換する

    Args:
        CurrentFilePath (str) : 相対パス

    Return:
        str: 絶対パス
    """
    data = os
    base = data.path.dirname(sys.argv[0])
    name = data.path.normpath(data.path.join(base, CurrentFilePath))
    return name


def Read(CurrentFilePath: str):
    """
    テキストファイルの読み込みをする

    Args:
        CurrentFilePath (str) : 相対パス

    Return:
        読み込んだファイルのテキストデータ
    """
    path = ConvertFileLink(CurrentFilePath)
    Files = open(path, "r", encoding="utf-8-sig")
    result = Files.read()
    Files.close()
    return result


def ReadCSV(CurrentFilePath):
    """
    CSVファイルを読み込み2次元配列を返す

    Args:
        CurrentFilePath (str) : 相対パス

    Return:
        2次元配列にしたCSVファイルのデータ
    """
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
    """
    テキストファイルに書き込む

    Args:
        CurrentFilePath (str)   : 相対パス
        WriteString     (str)   : 書き込むテキストデータ
        FileReadMode    (str)   : ファイルの読み込みモード
    """
    path = ConvertFileLink(CurrentFilePath)
    Files = open(path, FileReadMode, encoding="UTF-8")
    Files.write(WriteString)
    Files.close()


def WriteAdd(CurrentFilePath, WriteString):
    """
    テキストファイルに書き込む (追記)

    Args:
        CurrentFilePath (str)   : 相対パス
        WriteString     (str)   : 書き込むテキストデータ
    """
    Write(CurrentFilePath, WriteString, "a")


def WriteNew(CurrentFilePath, WriteString):
    """
    テキストファイルに書き込む (上書き)

    Args:
        CurrentFilePath (str)   : 相対パス
        WriteString     (str)   : 書き込むテキストデータ
    """
    Write(CurrentFilePath, WriteString, "w")


def Clear(CurrentFilePath):
    """
    テキストファイルの中身をクリアする

    Args:
        CurrentFilePath (str)   : 相対パス
    """
    WriteNew(CurrentFilePath, "")
