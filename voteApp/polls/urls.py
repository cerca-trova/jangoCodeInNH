from django.urls import path
from polls import views

#为应用添加命名空间，同其他应用区别开来
app_name = 'polls'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote, name='vote'),
]