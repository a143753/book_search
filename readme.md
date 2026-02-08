OpenBDから書籍情報を得るscript。

# 導入
## 

python3 -m venv venv
pip3 install requests

## Templaterをinstallしenable。
## Templaterの設定

Enable user system command functions.
User function no.xに追加
Function name : book search
System command : ${pythonへのpath}


( cd /Users/kazuh/Program/book_search; source ./venv/bin/activate; python3 get_book_info.py )

/bin/zsh /Users/kazuh/Program/book_search/get_book_info.zsh
