import os

# movie-plus ඇතුළේ තියෙන සියලුම .html files පරීක්ෂා කරයි
for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.lower().endswith(".html"):
            filepath = os.path.join(root, filename)
            
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # .png සහ .jpg links ඔක්කොම .webp වලට මාරු කිරීම
            new_content = content.replace(".png", ".webp").replace(".jpg", ".webp").replace(".jpeg", ".webp")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
                
            print(f"Updated HTML: {filepath}")