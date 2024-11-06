from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="collections"
    )
    tags = models.ManyToManyField(Tag, blank=True)
    ups = models.ManyToManyField(User, related_name="collection_upvotes", blank=True)
    downs = models.ManyToManyField(
        User, related_name="collection_downvotes", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Piece(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name="pieces"
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="pieces"
    )
    collections = models.ManyToManyField(Collection, blank=True, related_name="pieces")
    code = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    ups = models.ManyToManyField(User, related_name="piece_upvotes", blank=True)
    downs = models.ManyToManyField(User, related_name="piece_downvotes", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
