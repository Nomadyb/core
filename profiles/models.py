from django.db import models

from django.contrib.auth.models import User 
from PIL import Image
# Create your models here.



class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    bio = models.CharField(max_length=300, blank=True,null=True)
    city = models.CharField(max_length=100, blank=True,null=True)
    image = models.ImageField(null=True,blank=True,upload_to="profiles_photo/%Y/%m/")


    class Meta:
        verbose_name_plural = "Proffiller"

    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
        #ımage resize
        super().save(*args,**kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.image.path)





class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile,on_delete = models.CASCADE) #bir kullanıcı birden fazla  durum mesajına sahip olabilir.
    status_message = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Profil Durumları"

    def __str__(self):
        return str(self.user_profile) # str getirmelisin yoksa objeyi döndürür
