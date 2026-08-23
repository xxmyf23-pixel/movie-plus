import os
from PIL import Image

# movie-plus folder එක ඇතුළේ තියෙන සියලුම subfolders පරීක්ෂා කරයි
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(root, filename)
            
            try:
                img = Image.open(img_path)
                new_filename = os.path.splitext(filename)[0] + ".webp"
                new_path = os.path.join(root, new_filename)
                
                # WebP බවට Convert කිරීම (Quality 80%)
                img.save(new_path, "WEBP", quality=80)
                
                # Original PNG/JPG file එක එකපාරම Delete කිරීම
                os.remove(img_path)
                print(f"Converted & Deleted: {img_path}")
            except Exception as e:
                print(f"Error: {img_path} - {e}")