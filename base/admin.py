from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.admin import ModelAdmin

from .models import Collection, Tag, Language, Piece

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(Piece)
class PieceAdmin(ModelAdmin):
    list_display = ["id", "title", "language", "owner"]
    list_filter = ["language", "owner", "tags"]

@admin.register(Collection)
class CollectionAdmin(ModelAdmin):
    list_display = ["id", "name", "owner"]
    list_filter = ["owner", "tags"]


@admin.register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = ["id", "name"]
