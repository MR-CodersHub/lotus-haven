import glob

html_files = ["index.html"] + glob.glob("pages/*.html")
print(f"Aligning {len(html_files)} HTML files...")

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Replace layout text-left with text-start for menus and components
    content = content.replace("text-left shadow-soft", "text-start shadow-soft")
    content = content.replace("w-full text-left py-2", "w-full text-start py-2")
    content = content.replace("lg:text-left", "lg:text-start")
    content = content.replace("md:text-left", "md:text-start")
    content = content.replace("sm:text-left", "sm:text-start")
    content = content.replace("text-left space-y-", "text-start space-y-")
    content = content.replace("text-left mb-", "text-start mb-")
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  --> Updated: {filepath}")
    else:
        print(f"  --> No changes: {filepath}")

print("Alignment update completed!")
