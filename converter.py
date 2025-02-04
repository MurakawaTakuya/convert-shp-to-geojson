import os
import subprocess

dir_name = "Terminal2"
src_path = "./src/" + dir_name
dest_path = "./output/" + dir_name

input_dir = os.path.join(os.getcwd(), src_path)
output_dir = os.path.join(os.getcwd(), dest_path)

preserve_structure = False  # True の場合はディレクトリ構造を保持

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for root, dirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith(".shp"):
            shp_file = os.path.join(root, file)
            if preserve_structure:
                relative_path = os.path.relpath(root, input_dir)
                output_subdir = os.path.join(output_dir, relative_path)
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)
            else:
                output_subdir = output_dir
            base_name = os.path.splitext(file)[0]
            output_file = os.path.join(output_subdir, f"{base_name}.geojson")

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
