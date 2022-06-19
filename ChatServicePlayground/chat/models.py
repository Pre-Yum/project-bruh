from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Rooms(models.Model):
    name = models.CharField(max_length=254, blank=True, null = True , unique=True)



class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField(null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    room_name = models.ForeignKey('Rooms', on_delete=models.CASCADE)
 
    
    def __str__(self):
        return self.author.username
    
    
    
    def last_10_messages(self, id='lobby',m=[0,20]):
        print(m)
        
        room, created = Rooms.objects.get_or_create(name = id)
        
            
        len_msg = len(Message.objects.order_by('-timestamp').filter(room_name=room)[::])
        
        if (len_msg <= m[1]) :
            m[1] = len_msg  
            
             
        return  Message.objects.order_by('-timestamp').filter(room_name=room)[m[0]:m[1]:]
