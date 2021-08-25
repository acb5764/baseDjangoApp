from django.db import models
from django.contrib.auth.models import User 
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') 

    def __str__ (self):
        return f'{self.user.username} Profile'

    def save(self):#Resize profile pictures to save space
        super().save()

        img = Image.open(self.image.path) #opens the image in the current instance
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            #resizes the image
            #we should delete old images when new images are uploaded but whatever


#this is a change to a model which means we need to migrate if you make any changes
#to do so:
#python manage.py makemigrations
#python manage.py migrate