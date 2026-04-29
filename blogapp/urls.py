from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [

    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail,
         name='post_detail'),
    # path('<int:post_id>/share/', views.post_share, name='post_share'),
]
# repostry linki ni tashlash kk
# from django.views.generic import TemplateView
# from django.conf.urls import patterns, url
#
# urlpatterns = (patterns('my_app.views',
#         urls(r'^static/', TemplateView.as_view(template_name='static.html')),)
#
# 2 ta url kk post 1 tasi list 2 chisi deteilga
# deteil urlni nameni post_deteil deb nomlash kk absolute_urldagi bn bir xil bo'lishi kk
#funcsiya bo'lsa funcsiya nomi yoziladi
# class bo'lsa as_view deb () qavs ochib yopib qo'yiladi ),)
# 1 .28.47
