from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
Upon User creation, Profile model is added and connected to a single user
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_access = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
