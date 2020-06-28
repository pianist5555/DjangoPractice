from polls import views
from django.urls import path

app_name = 'polls' # 구분을 위한 namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # view 함수 호출시 views.detail(request, question_id = 'parameter')로 대응됨
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]