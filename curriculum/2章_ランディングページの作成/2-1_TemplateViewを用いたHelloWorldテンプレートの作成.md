# 2-1_TemplateViewを用いたHelloWorldテンプレートの作成

## まずは簡単なハローワールドを作成
前章で少し触れましたが、テンプレートとはクライアント(ブラウザ)に返すHTMLファイルの雛形です。テンプレートは.htmlファイルとして作成し、中のコードは基本的にはHTMLですが、if文やFor分といったプログラムも記載できます。それらのプログラム部分は、ページをブラウザに返す前にdjangoが処理を行い、最終的にはピュアなHTMLファイルが返されるような仕組みになっております。

では、早速テンプレートを作成しましょう。次にテンプレートを保管する場所ですが、前章のsettings.pyのTEMPLATES項目で指定したフォルダ内に配置するのですが、慣習としてアプリごとのサブディレクトリを作成して、その下にそのアプリのテンプレートを置くことが多い(名前の衝突を防ぐため)ので、そのようにします。

techpit/templatesの下にamazonフォルダを作成し、その中にlp.htmlというファイルを作成します。

```
techpit/
　 ├ amazon/
　 ├ static/
　 ├ manage.py
　 ├ templates/ 
 　　└ amazon/ # 新規作成
　　　　└ lp.html # 新規作成
```

後ほどしっかりと作りこみますが、現段階では以下の様な簡単なテキストファイルとします。

lp.html #新規作成
```html
hello world
```

後ほど詳細は作り込むこととして、ひとまずテンプレートの作成が完了です。

以上で今回のパートは終了です。

お疲れ様でした。
