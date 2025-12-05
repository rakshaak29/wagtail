import os
import django
import sys
from django.test import RequestFactory

# Setup Django environment
sys.path.append('/Users/rakshaak/Desktop/wagtail/mini-cms')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings.dev')
django.setup()

from home.views import custom_blocks_page_view
from home.models import HomePage

print("--- Debugging View ---")
factory = RequestFactory()
request = factory.get('/custom-blocks/')

# Call the view
try:
    response = custom_blocks_page_view(request)
    print(f"Response status: {response.status_code}")
    
    # Inspect context if possible (response.context_data is available for TemplateResponse)
    # But render() returns HttpResponse, so we might need to mock render or inspect content
    content = response.content.decode('utf-8')
    print(f"Response content length: {len(content)}")
    
    # Check if specific strings are in the content
    if "No blocks found" in content:
        print("FAILURE: 'No blocks found' message is present.")
    else:
        print("SUCCESS: 'No blocks found' message is NOT present.")
        
    # Let's inspect what the view logic actually does
    page = HomePage.objects.first()
    print(f"Page in DB: {page}")
    print(f"Page Body in DB: {page.body}")
    print(f"Page Body List: {list(page.body)}")

except Exception as e:
    print(f"Error calling view: {e}")
