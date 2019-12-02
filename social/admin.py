from django.contrib import admin
from . models import Profile,Post, PostLike, PostComment, PostFollow
from django.contrib.admin.options import ModelAdmin

class PostFollowAdmin(ModelAdmin):
    list_display =["profile","followed_by"]
    search_fields = ["profile","followed_by"]
    list_filter = ["profile","followed_by"]
admin.site.register(PostFollow,PostFollowAdmin)

class PostAdmin(ModelAdmin):
    list_display =["subject","created_at","uploaded_by"]
    search_fields = ["subject","message","uploaded_by"]
    list_filter = ["created_at","uploaded_by"]
admin.site.register(Post,PostAdmin)

class ProfileAdmin(ModelAdmin):
    list_display =["name"]
    search_fields = ["name","status","phone"]
    list_filter = ["gender","status"]
admin.site.register(Profile, ProfileAdmin)

class PostCommentAdmin(ModelAdmin):
     list_display =["post","message"]
     search_fields = ["message","post","commented_by"]
     list_filter = ["created_at"]
admin.site.register(PostComment,PostCommentAdmin)

class PostLikeAdmin(ModelAdmin):
    list_display =["post","liked_by"]
    search_fields = ["post","liked_by"]
    list_filter = ["created_at"]
admin.site.register(PostLike,PostLikeAdmin)

