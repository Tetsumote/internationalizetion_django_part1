from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

from django.utils.translation import gettext_lazy as _ 

from parler.models import TranslatableModel, TranslatedFields

class Post(TranslatableModel):

    translations = TranslatedFields(
        title = models.CharField(_('title'), max_length=250, db_index=True),
        body = models.TextField(_('body'), db_index=True),
    )
    
    author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='blog_posts',
                            verbose_name=_('author'),)
    publish = models.DateTimeField(_('publish'),default=timezone.now)
    created = models.DateTimeField(_('created'),auto_now_add=True)
    updated = models.DateTimeField(_('updated'),auto_now=True)

    def __str__(self):
        return self.title
