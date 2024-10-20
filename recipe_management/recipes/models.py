from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Dessert', 'Dessert'),
        ('Main Course', 'Main Course'),
        # Add other categories
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.JSONField()  # Store list of ingredients
    instructions = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    preparation_time = models.IntegerField()  # In minutes
    cooking_time = models.IntegerField()  # In minutes
    servings = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
