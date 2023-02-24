from hashlib import md5
from math import ceil
import random
import requests
from django.shortcuts import redirect
from django.shortcuts import render
from main.models import *
import re
from django.http.response import JsonResponse


def get_random_number(random_len):
    random_len = int(random_len)
    a = pow(10, random_len)
    b = pow(10, random_len - 1)
    n = random.randint(b, a)
    return n


def send_message(phone, sms):
    sms_domain = 'https://smsc.kz/sys/send.php'
    sms_params = {
        'login': 'rakhmetovmurod',
        'psw': '283746Mu',
        'mes': sms,
        'fmt': 3,
        'phones': phone,
    }
    r = requests.post(sms_domain, data=sms_params)
    print(r.status_code)
    print(r.json())
    print(phone)
    print(sms)


email_regex = re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
phone_regexp = re.compile(r'^77[0-9]{9}$')
iin_regexp = re.compile(r'[0-9]{12}$')


def indexHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))

    slider = Category.objects.all()
    course = Course.objects.all()
    best_teachers = Teacher.objects.filter(best_teacher=True)
    teachers = Teacher.objects.all()
    news = News.objects.all()
    testimonials = Testimonials.objects.all()
    about = AboutCompany.objects.all()

    return render(request, 'index.html', {
        'slider': slider,
        'course': course,
        'best_teachers': best_teachers,
        'news': news,
        'testimonials': testimonials,
        'about': about,
        'teachers': teachers,
        'active_user': active_user,
        'user_id': user_id,
    })


def aboutHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))

    about = AboutCompany.objects.all()
    assistant = Teacher.objects.filter(assistant=True)
    teachers = Teacher.objects.all()
    return render(request, 'about.html', {
        'about': about,
        'assistant': assistant,
        'teachers': teachers,
        'active_user': active_user,
        'user_id': user_id,
    })


def courseHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
    teachers = Teacher.objects.all()
    sort = request.GET.get('sort', 'all')
    about = AboutCompany.objects.all()

    if sort == 'offline':
        courses = Course.objects.filter(type_course__name="Offline")
    elif sort == 'online':
        courses = Course.objects.filter(type_course__name="Online")
    else:
        courses = Course.objects.all()

    limit = request.GET.get('limit', 3)
    current_page = int(request.GET.get('page', 1))
    total = len(courses)
    pages_count = ceil(total / limit)
    pages = range(1, pages_count + 1)
    stop = current_page * limit
    start = stop - limit
    prev_page = current_page - 1
    next_page = None
    if current_page < pages_count:
        next_page = current_page + 1

    return render(request, 'all-course.html', {
        'courses': courses[start:stop],
        'pages': pages,
        'prev_page': prev_page,
        'next_page': next_page,
        'current_page': current_page,
        'sort': sort,
        'teachers': teachers,
        'about': about,
        'active_user': active_user,
        'user_id': user_id,
    })


def teachersHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
    teacher = Teacher.objects.all()
    teachers = Teacher.objects.all()
    about = AboutCompany.objects.all()
    return render(request, 'all-teachers.html', {
        'teacher': teacher,
        'teachers': teachers,
        'about': about,
        'active_user': active_user,
        'user_id': user_id,
    })


def teacherItemHandler(request, teacher_id):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
    active_teacher = Teacher.objects.get(id=teacher_id)
    courses = Course.objects.filter(teacher__id=teacher_id)
    len_course = len(courses)
    teachers = Teacher.objects.all()
    about = AboutCompany.objects.all()

    return render(request, 'teacher-single.html', {
        'active_teacher': active_teacher,
        'courses': courses,
        'len_course': len_course,
        'teachers': teachers,
        'about': about,
        'active_user': active_user,
        'user_id': user_id,
    })


def courseItemHandler(request, course_id):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
    active_course = Course.objects.get(id=course_id)
    teachers = Teacher.objects.all()
    about = AboutCompany.objects.all()

    return render(request, 'course-single.html', {
        'active_course': active_course,
        'teachers': teachers,
        'about': about,
        'active_user': active_user,
        'user_id': user_id,
    })


def contactHandler(request):
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
    user_session_id = request.session.session_key

    about = AboutCompany.objects.all()
    course = Course.objects.all()
    teachers = Teacher.objects.all()
    action = request.POST.get('action', '')
    return_url = request.POST.get('return_url', '')

    if request.POST:
        if action == "sendForContact":
            send = SendMessage()
            send.name = request.POST.get('name', '')
            send.email = request.POST.get('email', '')
            send.text = request.POST.get('message', '')
            send.course = Course.objects.get(id=request.POST.get('course', 0))
            send.save()
        elif action == "sendForTeacher":
            send = SendMessageForTeacher()
            send.name = request.POST.get('name', '')
            send.email = request.POST.get('email', '')
            send.text = request.POST.get('message', '')
            send.save()
        elif action == 'add_to_wish_list':
            course_id = int(request.POST.get('course_id', 0))
            wish_items = WishItem.objects.filter(course__id=course_id, session_id=user_session_id)
            if wish_items:
                pass
            else:
                wish_item = WishItem()
                wish_item.session_id = active_user
                wish_item.course_id = course_id
                wish_item.save()

        return redirect(return_url)  # that's if we don't want to send again the form

    search_items = []
    q = request.GET.get('q', None)
    if q:
        search_items = Course.objects.filter(name__contains=q)

    return render(request, 'contact.html', {
        'about': about,
        'course': course,  # corrected the whitespace character
        'teachers': teachers,
        'search_items': search_items,
        'active_user': active_user,
        'user_id': user_id,
    })


def searchHandler(request):
    about = AboutCompany.objects.all()
    teachers = Teacher.objects.all()
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
    search_items = []
    q = request.GET.get('q', None)
    if q:
        search_items = Course.objects.filter(name__contains=q)

    return render(request, 'search.html', {
        'about': about,
        'teachers': teachers,
        'search_items': search_items,
        'q': q,
        'active_user': active_user,
        'user_id': user_id,
    })


def loginHandler(request):
    about = AboutCompany.objects.all()
    teachers = Teacher.objects.all()

    post_error = ''
    if request.POST:
        login = request.POST.get('login', '')
        password = request.POST.get('password', '')
        if login and password:
            temp_hash = md5()
            temp_hash.update(password.encode())
            password_hash = temp_hash.hexdigest()

            site_user = SiteUser.objects.filter(phone=login, password=password_hash)
            if not site_user:
                site_user = SiteUser.objects.filter(email=login, password=password_hash)

            if site_user:
                site_user = site_user[0]
                request.session['user_id'] = site_user.id
                return redirect('/')
            else:
                post_error = "USER_NOT_FOUND"
        else:
            post_error = "ERROR ARGUMENTS"

    return render(request, 'login.html', {
        'about': about,
        'teachers': teachers,
        'post_error': post_error,
    })


def logoutHandler(request):
    about = AboutCompany.objects.all()
    teachers = Teacher.objects.all()

    request.session['user_id'] = None
    redirect('/')

    return render(request, 'logout.html', {
        'about': about,
        'teachers': teachers,
    })


def registerHandler(request):
    about = AboutCompany.objects.all()
    teachers = Teacher.objects.all()
    if request.POST:
        phone = request.POST.get('phone', '')
        if phone:
            if len(phone) == 11:
                site_user = SiteUser.objects.filter(phone=phone)
                if site_user:
                    new_site_user = site_user[0]
                    old_password = str(get_random_number(4))
                    print(old_password)
                    password_hash = md5()
                    password_hash.update(old_password.encode())
                    new_password = password_hash.hexdigest()

                    new_site_user.password = new_password
                    new_site_user.save()
                    message = "Код для регистрация: " + str(old_password)
                    send_message(phone, message)
                    return redirect('/')
                else:
                    new_site_user = SiteUser()
                    new_site_user.phone = phone

                    old_password = str(get_random_number(4))
                    print(old_password)
                    password_hash = md5()
                    password_hash.update(old_password.encode())
                    new_password = password_hash.hexdigest()

                    new_site_user.password = new_password
                    new_site_user.save()
                    message = "Код для регистрация: " + str(old_password)
                    send_message(phone, message)
                    return redirect('/')
            else:
                print("FORMAT ERROR")
        else:
            print("NO ARGUMENT")

    return render(request, 'register.html', {
        'about': about,
        'teachers': teachers,
    })


def editHandler(request):
    about = AboutCompany.objects.all()
    teachers = Teacher.objects.all()

    user_id = request.session.get('user_id', None)
    active_user = None
    post_errors = []

    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
        if request.POST:
            last_name = request.POST.get('last_name', '')
            first_name = request.POST.get('first_name', '')
            middle_name = request.POST.get('middle_name', '')
            iin = request.POST.get('iin', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            active_password = request.POST.get('active_password', '')
            new_password = request.POST.get('new_password', '')
            new_password_repeat = request.POST.get('new_password_repeat', '')

            active_user.last_name = last_name
            active_user.first_name = first_name
            active_user.middle_name = middle_name

            if iin:
                if iin_regexp.match(iin):
                    active_user.iin = iin
                else:
                    post_errors.append("IIN_FORMAT_ERROR")
            if email:
                if email_regex.match(email):
                    email_users = SiteUser.objects.filter(email=email)
                    if email_users:
                        email_users = email_users[0]
                        if email_users.id == active_user.id:
                            pass
                        else:
                            post_errors.append("EMAIL_REGISTERED")
                    else:
                        active_user.email = email
                else:
                    post_errors.append("EMAIL_FORMAT_ERROR")
            if phone:
                if phone_regexp.match(phone):
                    phone_users = SiteUser.objects.filter(phone=phone)
                    if phone_users:
                        email_user = phone_users[0]
                        if email_user.id == active_user.id:
                            pass
                        else:
                            post_errors.append('PHONE_REGISTERED')
                    else:
                        active_user.phone = phone
                else:
                    post_errors.append('PHONE_FORMAT_ERROR')
            if active_password and new_password and new_password_repeat:
                temp_hash = md5()
                temp_hash.update(active_password.encode())
                active_password_hash = temp_hash.hexdigest()
                if active_user.password == active_password_hash:
                    if new_password == new_password_repeat:
                        new_temp_hash = md5()
                        new_temp_hash.update(new_password.encode())
                        new_password_hash = new_temp_hash.hexdigest()
                        active_user.password = new_password_hash
                    else:
                        print("NEW_PASSWORD_INCORRECT")
                else:
                    post_errors.append("ACTIVE_PASSWORD_INCORRECT")
            active_user.save()

    return render(request, 'edit.html', {
        'about': about,
        'teachers': teachers,
        'user_id': user_id,
        'active_user': active_user,
        'post_errors': post_errors,
    })


def wishHandler(request):
    about = AboutCompany.objects.all()
    teachers = Teacher.objects.all()
    user_session_id = request.session.session_key
    wish_list = []
    user_id = request.session.get('user_id', None)
    active_user = None
    if user_id:
        active_user = SiteUser.objects.get(id=int(user_id))
    if user_session_id:
        wish_list = WishItem.objects.filter(session_id=active_user)

    return render(request, 'wish.html', {
        'about': about,
        'teachers': teachers,
        'wish_list': wish_list,
        'active_user': active_user,
        'user_id': user_id,
    })
