from django.shortcuts import render
#from __future__ import unicode_literals
import uuid

from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Create your views here.
class News(models.Model):
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL, related_name='publisher', verbose_name='user')
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name='thread', verbose_name='related')
    content = models.TextField(verbose_name='main_content')
    reply = models.BooleanField(default=False, verbose_name='comment?')
    create_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='create time')

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        super(News, self).save(*args,**kwargs)
        if not self.reply:
            def save(self, *args, **kwargs):
                super(News, self).save(*args, **kwargs)

                if not self.reply:
                    channel_layer = get_channel_layer()
                    payload = {
                        "type": "receive",
                        "key": "additional_news",
                        "actor_name": self.user.username
                    }

    def get_parent(self):
        if self.parent:
            return self.parent
        else:
            return self

    def reply_this(self, user, text):
        parent = self.get_parent()
        News.objects.create(
            user=user,
            content=text,
            reply=True,
            parent=parent
        )

    def get_thread(self):
        parent = self.get_parent()
        return parent.thread.all()

    def comment_count(self):
        return self.get_thread().count()