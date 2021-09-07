from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField(null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(self, id='lobby'):
        return Message.objects.order_by('-timestamp').filter(room_name=id)[::-1]
