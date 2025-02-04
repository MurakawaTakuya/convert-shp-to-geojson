このプログラムは`.shp`ファイルを`.geojson`ファイルに変換するプログラム  
`/src`に入れた`.shp`ファイルを`/output`に`.geojson`ファイルとして出力する

# 準備
変換にはogr2ogrを使用する  
[OSGeo4W](https://trac.osgeo.org/osgeo4w/)からインストールできる

# 使い方
1. `/src`に`.shp`ファイルを入れる
2. `dir_name`に`/src`のディレクトリ名を入れる
3. ディレクトリ構造を保って変換したい場合は`preserve_structure`をtrueにする(falseの場合は`/output/dir_name`に展開される)
4. プログラムを実行して変換
