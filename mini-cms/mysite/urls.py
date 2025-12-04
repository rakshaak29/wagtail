from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from search import views as search_views

# 👉 Add this import
from home.views import custom_blocks_page_view


urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 👉 ADD YOUR CUSTOM PAGE URL HERE (VERY IMPORTANT)
urlpatterns += [
    path("custom-blocks/", custom_blocks_page_view, name="custom_blocks_page"),
]

# 👉 KEEP WAGTAIL LAST
urlpatterns += [
    path("", include(wagtail_urls)),
]