from django.db import models
from django.template.defaultfilters import slugify
# from taggit.managers import TaggableManager

from django.utils.translation import ugettext_lazy as _


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    image = models.ImageField()
    # tags = TaggableManager()
    tags = models.ManyToManyField("Tag", related_name="articles")
    content = models.TextField(verbose_name=_('content'))
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value,)
        super().save(*args, **kwargs)
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
