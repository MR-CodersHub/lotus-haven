import glob
import re

html_files = ["index.html"] + glob.glob("pages/*.html")
print(f"Scanning {len(html_files)} HTML files for mobile RTL toggle removal...")

pattern = re.compile(
    r'\s*<!-- RTL Toggle in Mobile Menu -->\s*'
    r'<button type="button" data-action="toggle-rtl" class="flex items-center gap-3 text-sm font-medium text-slate-700 dark:text-slate-200 hover:text-primary-600 transition-colors w-full text-start py-2" aria-label="Toggle layout direction">\s*'
    r'<span class="w-5 h-5 flex items-center justify-center font-semibold text-xs text-slate-400 dark:text-slate-500">\s*'
    r'RTL\s*'
    r'</span>\s*'
    r'<span>Toggle Direction</span>\s*'
    r'</button>',
    re.DOTALL
)

count = 0
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content, num_subs = pattern.subn('', content)
    
    if num_subs > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  --> Removed from: {filepath}")
        count += 1
    else:
        print(f"  --> No changes: {filepath}")

print(f"Removed mobile RTL toggle from {count} files!")
