from django.contrib import admin
from .models import BlogPost
from django.contrib.auth.models import Group,User
from django.utils.html import format_html

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','Content','create_date']
    list_filter = ('create_date',)
    search_fields = ('title',)
    list_per_page = 3
    date_hierarchy = 'create_date'
    list_display_links = ('Content',)
    list_editable = ('title',)
    def Content(self,obj):
        return format_html (f'<span style="color:red;">{obj.content}</span>')

    
    
admin.site.register(BlogPost,BlogAdmin)

# Register your models here.
admin.site.site_header = 'Blogging Admin Panel'
admin.site.site_title = 'Admin panel'
admin.site.index_title = 'custom admin panel'
admin.site.unregister(Group)
admin.site.unregister(User)



