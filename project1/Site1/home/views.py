import mimetypes
import os.path

from django.db import connection
from django.db.models.signals import post_save
from django_elasticsearch_dsl import signals
from django.shortcuts import render
from django.template.loader import render_to_string
from elasticsearch_dsl import Object
#    from django.db.models.signals import
#    from django.dispatch
from Site1.settings import BASE_DIR
from .models import Filee, Bil, Car
from django.http import HttpResponse
from ipware import get_client_ip
from django.core.mail import send_mail, EmailMessage
from django.db.models import Model
from .documents import CarDocument
import uuid
from django.core.cache import caches, cache


def download_test(request):
    filename = 'yourvideo.mp4'
    filepath = os.path.join(BASE_DIR, 'media/download/myvideo.mp4')
    path = open(filepath, 'rb')
    # mimetype = mimetypes.guess_type(filepath)
    response = HttpResponse(path)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response



'''
def start(request):
    # print(request.session.items())

    name = 'Ford'
    color = 'Blue'
    description = 'Wild and Fast'
    type = 1
    # توجه توجه: باید instanceی که به سیگنال سندر میدیم id داشته باشه وگرنع خودش یع آیدی چرت و برت میده بعد گند میزنه توش

    # car.save()      ممنوع شده توسط خامد موسوی
    insert_query = f"INSERT INTO home_car (name, color, description, type) VALUES ('{name}', '{color}', '{description}', {type})"
    select_query = f"SELECT * FROM home_car ORDER BY id DESC LIMIT 1"
    with connection.cursor() as cursor:
        cursor.execute(insert_query)
        cursor.execute(select_query)
        car_id = cursor.fetchone()[0]

    instance = Car(
        id=car_id,
        name=name,
        color=color,
        description=description,
        type=type
    )

    post_save.send(Car, instance=instance, created=True)
    s = CarDocument.search().filter('term', color='gray')
    qs = s.to_queryset()
    for c in qs:
        print(50 * '=')
        print(c.name)

    return render(request, 'email.html')
'''


def start(request):
    # cache.set('user_582_chars', 'KHEILI ZIAD')
    print(cache.get('user_582_chars'))
    return render(request, 'email.html')
















