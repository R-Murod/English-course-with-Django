from django.contrib import admin
from main.models import *


# Register your models here.
class AdminModelSingle(admin.ModelAdmin):
    pass


admin.site.register(Category, AdminModelSingle)
admin.site.register(Teacher, AdminModelSingle)
admin.site.register(Course, AdminModelSingle)
admin.site.register(Testimonials, AdminModelSingle)
admin.site.register(AboutCompany, AdminModelSingle)
admin.site.register(News, AdminModelSingle)
admin.site.register(SendMessage, AdminModelSingle)
admin.site.register(SendMessageForTeacher, AdminModelSingle)
admin.site.register(SiteUser, AdminModelSingle)
admin.site.register(WishItem, AdminModelSingle)
