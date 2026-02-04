<%*
// 1. ISBN入力
const isbn_input = await tp.system.prompt("ISBNを入力してください");
let output = "";
let bookTitle = isbn_input; // デフォルトはISBN

if (isbn_input) {
    // 2. Python実行
    // 引数として isbn_input を渡すと、設定画面の $1 に入り、そこから環境変数 isbn にセットされます
    output = await tp.user.get_book_info({isbn:isbn_input});
    
    // 3. タイトルの抽出とファイル名変更処理
    // Pythonが出力した "title: 本のタイトル" という行を探します
    const titleMatch = output.match(/^title:\s*(.*)$/m);
    if (titleMatch && titleMatch[1]) {
        bookTitle = titleMatch[1].trim();
        // ファイル名に使えない文字（: \ / ? " < > | *）を置換
        bookTitle = bookTitle.replace(/[:\\/?\"<>|*]/g, ' ');
    }
    
    // 4. リネームと移動（お好みのフォルダパスに変更してください）
    await tp.file.rename(bookTitle); 
    // ↓ "Inbox" フォルダなど、移動先が存在しないとエラーになるので注意してください
	await tp.file.move("Books/" + bookTitle); 
}
%>---
aliases:
<% output %>
---

## Reading Journey

