# 数値計算

数値計算に関する事項をまとめた資料．

## PDFのダウンロード方法

現在はベータ版を<https://github.com/calamari-dev/numcalc/releases>で配布しています．

## ライセンス

この資料は[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.ja)の下で配布しています．

## ビルド方法

以下は，この資料から派生する資料を作りたい方に向けた情報です．

PDFを生成するには，Pipenvと最新のTeX Liveがインストールされた環境で，次のコマンドを実行してください．

```
pipenv run ./publish.py
```

ただし，以下のフォントをあらかじめインストールしてください．

+ Liberation Sans（<https://github.com/liberationfonts/liberation-fonts>）
+ STIX Two Text（<https://www.stixfonts.org/>）
+ Source Han Serif（<https://source.typekit.com/source-han-serif/jp/>）
+ Source Han Sans（<https://source.typekit.com/source-han-sans/jp/>）

また，事前にjpbase.istをllmk.tomlと同じディレクトリに配置する必要があります．jpbase.istは[mendexのGitHubリポジトリ](https://github.com/texjporg/mendex-doc)から入手できます．
