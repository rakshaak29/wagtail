from django.shortcuts import render
from .models import CustomBlocksPage

def custom_blocks_page_view(request):
    # Load the first (and only) CustomBlocksPage instance
    page = CustomBlocksPage.objects.first()

    return render(request, "home/custom_content_blocks_page.html", {
        "page": page,
        "body": page.body if page else None,
    })
