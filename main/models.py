from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    posted_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200, blank=True)
    desc = models.TextField()
    logo = models.ImageField(upload_to='upload', blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    skype = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    best_teacher = models.BooleanField(default=False)
    assistant = models.BooleanField(default=False)
    experience = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    name = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(default=0, blank=True)
    desc1 = models.TextField()
    desc2 = models.TextField()
    duration = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    type_course = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    logo1 = models.ImageField(upload_to='upload', blank=True)
    logo2 = models.ImageField(upload_to='upload', blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    location_cart = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} {self.type_course}"


class Testimonials(models.Model):
    name = models.CharField(max_length=200, blank=True)
    desc = models.TextField()
    logo = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f"{self.name}"


class AboutCompany(models.Model):
    name = models.CharField(max_length=200, blank=True)
    name_author = models.CharField(max_length=200, blank=True)
    desc1 = models.TextField()
    desc2 = models.TextField()
    desc_footer = models.TextField()
    phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    linkedin = models.CharField(max_length=200, blank=True)
    logo_big = models.ImageField(upload_to='upload', blank=True)
    logo_author = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    name = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to='upload', blank=True)
    posted_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f"{self.name}"


class SendMessage(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class SendMessageForTeacher(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class SiteUser(models.Model):
    last_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    middle_name = models.CharField(max_length=200, blank=True)
    iin = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.phone


class WishItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0)  # 0 - created zakaz, -1 - otmeneen,  1 - confirmed, 2 - accepted

    def __str__(self):
        return f'{self.session_id} {self.course.name}'