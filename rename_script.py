import os
import re

directory = r"d:\MR-CodersHub\Front-end Projects\May Day\Yoga-Studio"

for root, dirs, files in os.walk(directory):
    if "node_modules" in root or ".git" in root:
        continue
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Case-preserving-ish replacements
            new_content = content.replace("Lotus Haven", "Lotus")
            new_content = new_content.replace("lotus haven", "lotus")
            new_content = new_content.replace("LOTUS HAVEN", "LOTUS")
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {path}")
