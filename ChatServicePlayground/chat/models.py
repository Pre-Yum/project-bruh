from django.db import models
from django.conf import settings
from friend.models import FriendList, FriendRequest
from account.models import Account

# Create your models here.
User = Account()

class Message(models.Model):
    #author = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True , help_text='users who are connected to the chat'),
    author = models.ForeignKey(Account, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.author

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10:-1]


