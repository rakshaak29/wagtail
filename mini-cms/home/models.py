from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from . import blocks as custom_blocks


# -----------------------------
# HOME PAGE
# -----------------------------
class HomePage(Page):
    body = StreamField(
        [
            ("faq", custom_blocks.FAQBlock()),
            ("testimonial", custom_blocks.TestimonialBlock()),
            ("cta", custom_blocks.CTABlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


# -----------------------------
# CUSTOM BLOCKS PAGE
# -----------------------------
class CustomBlocksPage(Page):
    template = "mini-cms/home/templates/home/custom_content_blocks_page.html.html"

    body = StreamField(
        [
            ("faq", custom_blocks.FAQBlock()),
            ("testimonial", custom_blocks.TestimonialBlock()),
            ("cta", custom_blocks.CTABlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Custom Blocks Page"