from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            phone_number=phone_number
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, nickname, phone_number, password=None):
        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
            phone_number=phone_number
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(max_length=10)
    phone_number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    follow = models.ManyToManyField('self', symmetrical=False, related_name = "followers")
    
    
    
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'phone_number', 'follow']
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin









