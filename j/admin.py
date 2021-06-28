from django.contrib import admin

from j.models import Member


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
   list_display=['name','mobilenumber','role','area']


admin.site.register(Member,MemberAdmin)

