from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse

# Create your models here.

# blog post model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=5000)
    date_time= models.DateField(default = timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("user/post_detail", kwargs={'pk': self.pk})
# user profile
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',height_field=None, width_field=None, upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # resize the image of user
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        # image resization of user profile pic
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)