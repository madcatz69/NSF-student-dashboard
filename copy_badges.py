import shutil
import glob
import os

source_pattern = r"C:\Users\vaman\.gemini\antigravity\brain\af3feb99-57cd-4583-83fc-ea780b5c9ab0\media__*.png"
dest_dir = r"d:\vaman\aggah\nsf student website\assets\badges"
os.makedirs(dest_dir, exist_ok=True)
files = glob.glob(source_pattern)
print(f"Found {len(files)} files.")
for f in files:
    try:
        shutil.copy(f, dest_dir)
        print(f"Copied {os.path.basename(f)}")
    except Exception as e:
        print(f"Failed {f}: {e}")
