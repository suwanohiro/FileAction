import sys
import os


def ConvertFileLink(CurrentFilePath: str) -> str:
    """
    相対パスを絶対パスに変換する

    Args:
        CurrentFilePath (str) : 相対パス

    Return:
        str: 絶対パス
    """
    base = os.path.dirname(sys.argv[0])
    name = os.path.normpath(os.path.join(base, CurrentFilePath))
    return name


def Read(CurrentFilePath: str) -> str:
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


def ReadCSV(CurrentFilePath: str) -> list[str]:
    """
    CSVファイルを読み込み2次元配列を返す

    Args:
        CurrentFilePath (str) : 相対パス

    Return:
        2次元配列にしたCSVファイルのデータ
    """
    TextData: str = Read(CurrentFilePath)
    Result: list[str] = []
    Array: list[str] = TextData.split("\n")

    for data in Array:
        work = data.split(",")
        Result.append(work)
    return Result


def Write(CurrentFilePath: str, WriteString: str, FileReadMode: str) -> None:
    """
    テキストファイルに書き込む

    Args:
        CurrentFilePath (str)   : 相対パス
        WriteString     (str)   : 書き込むテキストデータ
        FileReadMode    (str)   : ファイルの読み込みモード
    """
    path: str = ConvertFileLink(CurrentFilePath)
    Files = open(path, FileReadMode, encoding="UTF-8")
    Files.write(WriteString)
    Files.close()


def WriteAdd(CurrentFilePath: str, WriteString: str) -> None:
    """
    テキストファイルに書き込む (追記)

    Args:
        CurrentFilePath (str)   : 相対パス
        WriteString     (str)   : 書き込むテキストデータ
    """
    Write(CurrentFilePath, WriteString, "a")


def WriteNew(CurrentFilePath: str, WriteString: str) -> None:
    """
    テキストファイルに書き込む (上書き)

    Args:
        CurrentFilePath (str)   : 相対パス
        WriteString     (str)   : 書き込むテキストデータ
    """
    Write(CurrentFilePath, WriteString, "w")


def Clear(CurrentFilePath: str) -> None:
    """
    テキストファイルの中身をクリアする

    Args:
        CurrentFilePath (str)   : 相対パス
    """
    WriteNew(CurrentFilePath, "")
