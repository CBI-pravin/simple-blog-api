from django.db import models,IntegrityError
from django.contrib.auth.models import AbstractUser,UserManager

import uuid
# Create your models here.

class MyUserManager(UserManager):
    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=email, is_staff=True, is_superuser=True,**kwargs)
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractUser):
    username = None
    first_name = None
    last_name=None

    name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    likes = models.ManyToManyField(MyUser,related_name="likes",null=True,blank=True)


    # THIS METHOPD WILL GENERATE A RANDOM UUID FIELD FOR EACH POST
    def save(self, *args, **kwargs):
        while True:
            try:
                super().save(*args, **kwargs)
            except IntegrityError:
                # This ID already exists in the database, generate a new one
                self.id = uuid.uuid4()
            else:
                break

    def __str__(self):
        return self.title



class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_reply = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        while True:
            try:
                super().save(*args, **kwargs)
            except IntegrityError:
                # This ID already exists in the database, generate a new one
                self.id = uuid.uuid4()
            else:
                break

    def __str__(self) -> str:
        return self.content