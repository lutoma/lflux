from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _

from taggit.managers import TaggableManager


class Image(models.Model):
    img = models.ImageField(_('image'), upload_to='limage')

    tags = TaggableManager(blank=True, related_name='limages')

    object_id = models.PositiveIntegerField(null=True)
    content_type = models.ForeignKey(ContentType, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
