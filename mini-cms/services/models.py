from wagtail.models import Page
from home.models import HomePage

class ServicesPage(Page):
    template = "services/services_page.html"

    def get_context(self, request):
        context = super().get_context(request)

    # Load the REAL home page using the correct slug
        homepage = HomePage.objects.get(slug="home")

        context["home_body"] = homepage.body
        return context