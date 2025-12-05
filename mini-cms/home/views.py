from django.shortcuts import render
from .models import HomePage

def custom_blocks_page_view(request):
    # Find the HomePage that actually has content
    page = None
    blocks = []
    
    # Check all home pages
    for p in HomePage.objects.all():
        # Convert body to list to check if it has items
        current_blocks = list(p.body)
        if current_blocks:
            page = p
            blocks = current_blocks
            break  # Found the one with content!
    
    # If no content found, fallback to the first page (even if empty)
    if not page:
        page = HomePage.objects.first()
        blocks = []

    return render(request, "home/custom_content_blocks_page.html", {
        "page": page,
        "blocks": blocks,
    })