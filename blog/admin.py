from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # list_display attribute does what its name suggests display the properties mentioned in the tuple in the post list for each post.
    list_display=('title', 'slug', 'status', 'created_on')
    
    # filtering the post depending on their Status this is done by the list_filter method.
    list_filter = ('status',)

    # search bar at the top of the list, which will search the database from the search_fields
    search_fields = ['title', 'content']

    # prepopulated_fields populates the slug
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)