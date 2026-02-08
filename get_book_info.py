import sys
import os
import requests
import json
import io
import re

# 【重要】Windowsでの文字化けを防止するため、標準出力をUTF-8に強制設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_book_info(isbn_input):
    # 万が一環境変数が空だった場合のガード
    if not isbn_input:
        return {"found": False, "isbn": "No Input"}

    # ハイフン除去
    isbn = isbn_input.replace('-', '').strip()
    url = f"https://api.openbd.jp/v1/get?isbn={isbn}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # データがない場合
        if not data or data[0] is None:
            return {
                "found": False,
                "isbn": isbn,
                "cover": f"https://ndlsearch.ndl.go.jp/thumbnail/{isbn}.jpg"
            }
            
        book = data[0]['summary']
        
        # 著者名や書影の取得
        author = re.sub( r',', '', book.get('author', '') )
        cover = book.get('cover', '')
        if not cover:
            cover = f"https://ndlsearch.ndl.go.jp/thumbnail/{isbn}.jpg"
            
        return {
            "found": True,
            "title": book.get('title', ''), 
            "author": author,
            "publisher": book.get('publisher', ''),
            "pubdate": book.get('pubdate', ''),
            "isbn": book.get('isbn', isbn),
            "cover": cover
        }

    except Exception as e:
        print("unko")
        return {"found": False, "isbn": isbn}

if __name__ == "__main__":
    # 1. 環境変数からISBNを取得
    isbn_input = os.environ.get("isbn")
#    isbn_input = "9784344429727"

    info = get_book_info(isbn_input)
    
    if info.get("found"):
        # 【重要】タイトルをファイル名変更用にYAMLに出力
        print(f"title: {info['title']}")
        print(f"cover: {info['cover']}")
        print(f"tags:")
        print(f"author: \"[[{info['author']}]]\"")
        print(f"pages: ")
        print(f"ISBN: {info['isbn']}")
    else:
        # 見つからない場合も最低限出力
        print(f"title: {info['isbn']}") # タイトル代わりにISBNを入れる
        print(f"cover: {info['cover']}")
        print("tags:")
        print("author:")
        print("pages:")
        print(f"ISBN: {info['isbn']}")
