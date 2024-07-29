from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def get_absolute_url(self):
      return reverse("recipes-detail", kwargs={"pk": self.pk})


    def __str__(self):
      return self.title


class SavedRecipeModel(models.Model):
    author = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    posts = models.ManyToManyField(Recipe,related_name="SavedRecipeModel_posts",blank=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)