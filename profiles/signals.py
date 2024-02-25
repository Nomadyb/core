from django.contrib.auth.models import User 
from profiles.models import Profile , ProfileStatus
from django.db.models.signals import post_save # kayıttan sonra yani user kayıt edildikten sorna profil nesnesini kayıt etmek için 
from django.dispatch import receiver # decarator yapısı alıcıdır iki argüman alır ilk olarak işlem tanımlanır sonra alıcı tanımlanır


@receiver(post_save,sender=User) # user üzerinden bir nesne yaratılınca  insatance içinden tetikle ve profili create et 
def create_profil(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance) #her seferinde farklı bir user profili yaratılacak bu sebeple instance verilmelidir.


@receiver(post_save,sender=Profile)
def create_first_status_message(sender,instance,created,**kwargs):
    # print(instance.username,"__Created__",created)
    if created:
        ProfileStatus.objects.create(
            user_profile=instance, status_message=f"Hi {instance.user.username} , Welcome to the Internet")
