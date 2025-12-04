from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

# FAQ ITEM
class FAQItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.TextBlock(required=True)

    class Meta:
        icon = "help"
        label = "FAQ Item"


# FAQ BLOCK
class FAQBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, default="Frequently Asked Questions")
    items = blocks.ListBlock(FAQItemBlock())

    class Meta:
        template = "home/blocks/faq_block.html"
        icon = "help"
        label = "FAQ Block"


# TESTIMONIAL BLOCK
class TestimonialBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    role = blocks.CharBlock(required=False)
    photo = ImageChooserBlock(required=False)
    quote = blocks.TextBlock(required=True)

    class Meta:
        template = "home/blocks/testimonial_block.html"
        icon = "user"
        label = "Testimonial"


# CTA BLOCK
class CTABlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True)
    text = blocks.TextBlock(required=True)
    button_text = blocks.CharBlock(required=True, default="Learn more")
    button_link = blocks.URLBlock(required=True)

    class Meta:
        template = "home/blocks/cta_block.html"
        icon = "plus"
        label = "Call to Action"