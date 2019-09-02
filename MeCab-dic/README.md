# ユーザー辞書作成方法
### 参考
- [MeCab 単語の追加方法](https://taku910.github.io/mecab/dic.html)
- [mecabユーザ辞書を追加 - Qiita](https://qiita.com/takaheraw@github/items/286cdb27887bd00e2245)

### 辞書用のcsvファイル作成
```csv:/path/to/hoge.csv
# 表層形,左文脈ID,右文脈ID,コスト,品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
ほげ丸,,,1000,名詞,固有名詞,人名,名,*,*,ほげまる,ホゲマル,ホゲマル
```

### 辞書のコンパイル
- macの場合
  - `-d`: システム辞書があるディレクトリ
  - `-u`: ユーザファイルを作成
  - `-f`: csvの文字コード
  - `-t`: バイナリ辞書の文字コード
```bash
/usr/local/Celler/mecab/0.996/libexec/mecab/mecab-dict-index \
-d /usr/local/lib/mecab/dic/ipadic \
-u hoge.dic \
-f utf-8 \
-t utf-8 hoge.csv
```

### /usr/local/etc/mecabrcにパスを通す
```plain:/usr/local/etc/mecabrc
userdic = /path/to/test.dic
```
