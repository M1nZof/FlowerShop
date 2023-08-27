from django.urls import path, include
from flower_app import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:bouquet_id>/', views.card, name='card'),
    path('catalog/', views.catalog, name='catalog'),
    path('consultation/', views.consultation, name='consultation'),
    path('order/<int:bouquet_id>/', views.order, name='order'),
    path('order_step/<int:order_id>/', views.order_step, name='order_step'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz_step/', views.quiz_step, name='quiz_step'),
    path('result/', views.result, name='result'),
    path('tinymce/', include('tinymce.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
