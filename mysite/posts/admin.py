from django.contrib import admin

from .models import Posts

from .models import Posts

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'pub_date',
        'text',
        'image'
    )
    list_editable = ('text', )
    list_filter = ('pub_date', )


admin.site.register(Posts, PostAdmin)

