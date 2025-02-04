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

# データソース
[国土交通省 G空間情報センター](https://www.geospatial.jp/ckan/organization/seisakutokatsu)
- `ShinjukuTerminal`: [新宿駅周辺屋内地図オープンデータ（令和2年度更新版）](https://www.geospatial.jp/ckan/dataset/mlit-indoor-shinjuku-r2)
- `NagoyaUnimall`: [ユニモール地下街 屋内地図オープンデータ](https://www.geospatial.jp/ckan/dataset/city-nagoya-indoor-unimall)
- `NagoyaCentralPark`: [セントラルパーク地下街 屋内地図オープンデータ](https://www.geospatial.jp/ckan/dataset/city-nagoya-indoor-centralpark?resource_id=f803f525-bd47-44f3-8a99-9ad1a01205f8)
- `NaritaAirport`: [成田国際空港屋内地図オープンデータ（令和２年度更新版）](https://www.geospatial.jp/ckan/dataset/mlit-indoor-narita-airport-r2)
- `NissanStd`: [横浜国際総合競技場屋内地図オープンデータ](https://www.geospatial.jp/ckan/dataset/mlit-indoor-yokohama-arena)
- `Shinyokohama`: [新横浜駅屋内地図オープンデータ](https://www.geospatial.jp/ckan/dataset/mlit-indoor-shin-yokohama)
- `TokyoStation`: [東京駅周辺屋内地図オープンデータ（令和元年度版）](https://www.geospatial.jp/ckan/dataset/mlit-indoor-tokyo)
