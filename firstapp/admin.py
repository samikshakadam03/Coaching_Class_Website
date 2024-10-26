from django.contrib import admin
from.models import *
# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Gallery,GalleryAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display=['header','image']
admin.site.register(Result,ResultAdmin)

class NoticeAdmin(admin.ModelAdmin):
    list_display=['notice']
admin.site.register(Notice,NoticeAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display=['user','comment','rate','created_at']
admin.site.register(Review,ReviewAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','message']
admin.site.register(Contact,ContactAdmin)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'email', 'mobile', 'gender', 'address', 'board', 'std', 'sclname', 'scltime', 'marks')