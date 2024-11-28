from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [

        ('normal', 'Normal'),
        ('clarendon', 'Clarendon'),
        ('gingham', 'Gingham'),
        ('moon', 'Moon'),
        ('lark', 'Lark'),
        ('reyes', 'Reyes'),
        ('juno', 'Juno'),
        ('slumber', 'Slumber'),
        ('aden', 'Aden'),
        ('perpetua', 'Perpetua'),
        ('mayfair', 'Mayfair'),
        ('rise', 'Rise'),
        ('hudson', 'Hudson'),
        ('valencia', 'Valencia'),
        ('xpro2', 'X-Pro II'),
        ('willow', 'Willow'),
        ('lofi', 'Lo-Fi'),
        ('inkwell', 'Inkwell'),
        ('nashville', 'Nashville'),
        ('amaro', 'Amaro'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('sutro', 'Sutro'),
        ('toaster', 'Toaster'),
        ('walden', 'Walden'),
        ('1977', '1977'),
        ('kelvin', 'Kelvin'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'