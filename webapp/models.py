from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='webapp_user_set',  # Change related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='webapp_user_set',  # Change related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Deliverer(models.Model):
    
    full_name = models.CharField(max_length=100)
    
    age = models.PositiveIntegerField()
    
    address = models.CharField(max_length=300)
    
    phone_number = models.CharField(max_length=20)
    
    @property
    def is_working(self):
        return self.record_set.filter(status='on-going').exists()

    def __str__(self):
        
        return self.full_name

class Record(models.Model):
    
    STATUS_CHOICES = [
        ('on-going', 'On-Going'),
        ('completed', 'Completed'),
    ]

    creation_date = models.DateTimeField(auto_now_add=True)

    delivery_man = models.ForeignKey(Deliverer, on_delete=models.CASCADE)
    
    client_address = models.CharField(max_length=300)
        
    client_name = models.CharField(max_length=100)
    
    client_phone = models.CharField(max_length=20)
        
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='on-going')
    
    def __str__(self):

        return f"{self.status} : {self.delivery_man}"
    