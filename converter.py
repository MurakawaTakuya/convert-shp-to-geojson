import os
import glob
import subprocess

dir_name = "Terminal1"
src_path = "./src/" + dir_name
dest_path = "./output/" + dir_name

input_dir = os.path.join(os.getcwd(), src_path)

output_dir = os.path.join(os.getcwd(), dest_path)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

shp_files = glob.glob(os.path.join(input_dir, "*.shp"))

# 各 shapefile を GeoJSON に変換
for shp_file in shp_files:
    base_name = os.path.splitext(os.path.basename(shp_file))[0]
    output_file = os.path.join(output_dir, f"{base_name}.geojson")

    cmd = [
        "ogr2ogr",
        "-f", "GeoJSON",
        "-t_srs", "EPSG:6677",
        output_file,
        shp_file
    ]

    print(f"変換中: {shp_file} -> {output_file}")

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"変換に失敗しました: {shp_file}")
        print(e)
