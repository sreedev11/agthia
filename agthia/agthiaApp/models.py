from django.db import models

class Local(models.Model):
    image = models.ImageField(upload_to='local_images/')
    name = models.CharField(max_length=150, null=True,default='1')

    def __str__(self):
        return f'Local Image {self.id}: {self.name}'
    

    
class Registration(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    BRAND_CHOICES = (
        ('LOCAL', 'Local Brands'),
        ('INTERNATIONAL', 'International Brands'),
    )

    local = models.ForeignKey(Local, on_delete=models.CASCADE, default=1)
    brand_type = models.CharField(max_length=20, choices=BRAND_CHOICES,default='LOCAL')
    image1 = models.ImageField(upload_to='local_images/')
    image2 = models.ImageField(upload_to='local_images/')
    heading = models.CharField(max_length=200)
    description = models.TextField()
    additional_image1 = models.ImageField(upload_to='local_images/', blank=True, null=True)
    additional_image2 = models.ImageField(upload_to='local_images/', blank=True, null=True)
    additional_image3 = models.ImageField(upload_to='local_images/', blank=True, null=True)

    def __str__(self):
        return self.heading
    

class Inter(models.Model):
    image = models.ImageField(upload_to='local_images/')
    name = models.CharField(max_length=150, null=True,default='1')

    def __str__(self):
        return f'Inter Image {self.id}: {self.name}'
    

class Restaurant2(models.Model):
    BRAND_CHOICES = (
        ('LOCAL', 'Local Brands'),
        ('INTERNATIONAL', 'International Brands'),
    )

    inter = models.ForeignKey(Inter, on_delete=models.CASCADE, default=1)
    brand_type = models.CharField(max_length=20, choices=BRAND_CHOICES,default='LOCAL')
    image1 = models.ImageField(upload_to='local_images/')
    image2 = models.ImageField(upload_to='local_images/')
    heading = models.CharField(max_length=200)
    description = models.TextField()
    additional_image1 = models.ImageField(upload_to='local_images/', blank=True, null=True)
    additional_image2 = models.ImageField(upload_to='local_images/', blank=True, null=True)
    additional_image3 = models.ImageField(upload_to='local_images/', blank=True, null=True)

    def __str__(self):
        return self.heading
    

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name