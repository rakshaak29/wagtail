import os
import django
import sys

# Setup Django environment
sys.path.append('/Users/rakshaak/Desktop/wagtail/mini-cms')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.dev')
django.setup()

from home.models import HomePage

print("--- Testing Robust Logic ---")
found_page = None
found_blocks = []

all_pages = HomePage.objects.all()
print(f"Total pages: {all_pages.count()}")

for p in all_pages:
    print(f"Checking page ID {p.id}...")
    # Force evaluation of streamfield
    blocks = list(p.body)
    print(f"  Block count: {len(blocks)}")
    if blocks:
        found_page = p
        found_blocks = blocks
        print("  -> Found content!")
        break

if found_page:
    print(f"Selected Page ID: {found_page.id}")
    print(f"Selected Blocks: {len(found_blocks)}")
else:
    print("No page with content found.")
