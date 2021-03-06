# 数値計算

数値計算に関する事項をまとめた資料．

## PDFのダウンロード方法

現在はベータ版を<https://github.com/calamari-dev/numcalc/releases>で配布しています．なお，`main`ブランチにあるLaTeXソースは下書きやメモを含むため，誤りを含む可能性が多分にあります．そのため，内容に関するご指摘は最新のPDFに対してお願い致します．

## ライセンス

この資料は[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.ja)の下で配布しています．

## ビルド方法

以下は，この資料から派生する資料を作りたい方に向けた情報です．

PDFを生成するには，Pipenvと最新のTeX Liveがインストールされた環境で，次のコマンドを実行してください（`.vscode/settings.json`は環境変数`PIPENV_VENV_IN_PROJECT`の値が`1`であるもとで，次のコマンドを実行したと仮定して書いています）．

```
pipenv run ./publish.py
```

ただし，以下のフォントをあらかじめインストールしておいてください．

+ Liberation Sans（<https://github.com/liberationfonts/liberation-fonts>）
+ STIX Two Text（<https://www.stixfonts.org/>）
+ Source Han Serif（<https://source.typekit.com/source-han-serif/jp/>）
+ Source Han Sans（<https://source.typekit.com/source-han-sans/jp/>）
