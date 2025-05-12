# FileAction

`FileAction` は、Python でのファイル操作を簡単にするためのユーティリティ関数を提供するライブラリです。このライブラリを使用することで、ファイルの読み書きやクリア、CSV ファイルの操作などを簡単に行うことができます。

---

## 特徴 ✨

- **簡単なファイル操作**<br>
  テキストファイルや CSV ファイルの読み書きを簡潔に実装可能です。
- **柔軟なモード指定**<br>
  上書き、追記、クリアなどの操作をサポートします。
- **相対パス対応**<br>
  相対パスを絶対パスに変換する便利な関数を提供します。

---

## インストール 🚀

以下のコマンドでインストールできます。

```bash
pip install FileAction
```

---

## 使用方法 🛠️

以下は、`FileAction` の基本的な使用例です。

```python
import FileAction

# ファイルにデータを書き込む
FileAction.WriteNew("example.txt", "Hello, World!")

# ファイルの内容を読み込む
content = FileAction.Read("example.txt")
print(content)  # 出力: Hello, World!
```

---

## 提供される関数 📚

### 1. `ConvertFileLink(CurrentFilePath: str) -> str`

相対パスを絶対パスに変換します。

| 引数              | 型  | 説明     |
| ----------------- | --- | -------- |
| `CurrentFilePath` | str | 相対パス |

**戻り値**: 絶対パス (str)

---

### 2. `Read(CurrentFilePath: str) -> str`

指定されたテキストファイルを読み込み、その内容を文字列として返します。

| 引数              | 型  | 説明     |
| ----------------- | --- | -------- |
| `CurrentFilePath` | str | 相対パス |

**戻り値**: ファイルの内容 (str)

---

### 3. `ReadCSV(CurrentFilePath: str) -> list[str]`

CSV ファイルを読み込み、2 次元配列として返します。

| 引数              | 型  | 説明     |
| ----------------- | --- | -------- |
| `CurrentFilePath` | str | 相対パス |

**戻り値**: 2 次元配列 (list[str])

---

### 4. `Write(CurrentFilePath: str, WriteString: str, FileReadMode: str) -> None`

指定されたモードでテキストファイルにデータを書き込みます。

| 引数              | 型  | 説明                                        |
| ----------------- | --- | ------------------------------------------- |
| `CurrentFilePath` | str | 相対パス                                    |
| `WriteString`     | str | 書き込むデータ                              |
| `FileReadMode`    | str | ファイルモード (`"w"`: 上書き, `"a"`: 追記) |

---

### 5. `WriteAdd(CurrentFilePath: str, WriteString: str) -> None`

テキストファイルにデータを追記します。

| 引数              | 型  | 説明           |
| ----------------- | --- | -------------- |
| `CurrentFilePath` | str | 相対パス       |
| `WriteString`     | str | 書き込むデータ |

---

### 6. `WriteNew(CurrentFilePath: str, WriteString: str) -> None`

テキストファイルにデータを上書きします。

| 引数              | 型  | 説明           |
| ----------------- | --- | -------------- |
| `CurrentFilePath` | str | 相対パス       |
| `WriteString`     | str | 書き込むデータ |

---

### 7. `Clear(CurrentFilePath: str) -> None`

テキストファイルの内容をクリアします。

| 引数              | 型  | 説明     |
| ----------------- | --- | -------- |
| `CurrentFilePath` | str | 相対パス |

---

## 更新履歴 📝

### バージョン 1.0.0

- 初回リリース。
- 基本的なファイル操作機能を実装。
  - ファイルの読み込み (`Read`)
  - ファイルへの書き込み (`Write`, `WriteAdd`, `WriteNew`)
  - ファイルのクリア (`Clear`)
  - CSV ファイルの読み込み (`ReadCSV`)
  - 相対パスの絶対パス変換 (`ConvertFileLink`)

### 今後の予定

- エラーハンドリングの強化。
- JSON ファイルの読み書き機能の追加。
- ファイル操作の非同期対応。

---

## ライセンス 📄

このプロジェクトは [MIT ライセンス](LICENSE) のもとで公開されています。

---

## 貢献 🤝

バグ報告や機能リクエストは、[GitHub リポジトリ](https://github.com/your-repo/FileAction) にて受け付けています。プルリクエストも歓迎します！
