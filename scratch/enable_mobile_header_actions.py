import glob

html_files = ["index.html"] + glob.glob("pages/*.html")
print(f"Enabling mobile header actions in {len(html_files)} HTML files...")

old_rtl_class = 'class="btn-secondary !py-2.5 !px-4 !text-xs hidden md:inline-flex h-11 items-center"'
new_rtl_class = 'class="btn-secondary !py-2.5 !px-3 sm:!px-4 !text-xs inline-flex h-11 items-center"'

old_profile_class = 'class="hidden md:inline-flex h-11 w-11 items-center justify-center rounded-full border border-slate-300 bg-white text-slate-700 shadow-soft transition hover:border-primary-500 hover:bg-primary-50 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100"'
new_profile_class = 'class="inline-flex h-11 w-11 items-center justify-center rounded-full border border-slate-300 bg-white text-slate-700 shadow-soft transition hover:border-primary-500 hover:bg-primary-50 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100"'

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # 1. Update RTL toggle class
    content = content.replace(old_rtl_class, new_rtl_class)
    
    # 2. Update Profile toggle class
    content = content.replace(old_profile_class, new_profile_class)
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  --> Updated: {filepath}")
    else:
        print(f"  --> No changes: {filepath}")

print("Mobile header actions script execution completed!")
