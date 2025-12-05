import os
import django
import sys

# Setup Django environment
sys.path.append('/Users/rakshaak/Desktop/wagtail/mini-cms')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.dev')
django.setup()

from home.models import HomePage, CustomBlocksPage

print("--- Inspecting HomePage ---")
home_pages = HomePage.objects.all()
print(f"Found {home_pages.count()} HomePage(s)")
for p in home_pages:
    print(f"ID: {p.id}, Title: {p.title}, Slug: {p.slug}")
    print(f"Body type: {type(p.body)}")
    print(f"Body content: {p.body}")
    # Check if streamfield has items
    if hasattr(p.body, '__iter__'):
        print(f"Item count: {len(list(p.body))}")
    else:
        print("Body is not iterable")

print("\n--- Inspecting CustomBlocksPage ---")
custom_pages = CustomBlocksPage.objects.all()
print(f"Found {custom_pages.count()} CustomBlocksPage(s)")
for p in custom_pages:
    print(f"ID: {p.id}, Title: {p.title}, Slug: {p.slug}")
    print(f"Body content: {p.body}")
    if hasattr(p.body, '__iter__'):
        print(f"Item count: {len(list(p.body))}")

