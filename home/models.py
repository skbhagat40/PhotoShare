from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page


class HomePage(Page):
    page_heading = models.CharField(max_length=100)
    content_panels = Page.content_panels + [FieldPanel('page_heading', classname='full')]

    def get_context(self, request):
        context = super().get_context(request);
        context['items'] = self.get_children().live()
        return context

