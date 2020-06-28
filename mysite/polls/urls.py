from polls import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'polls' # 구분을 위한 namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # view 함수 호출시 views.detail(request, question_id = 'parameter')로 대응됨
    path('<int:question_id>/results', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('about/', MyView.as_view()) # class 클래스형으로 만들어주는 메소드 (진입메소드), 인스턴스생성 및 dispatch() 메소드 호출 역할
    path('abouts/', TemplateView.as_view(template_name="about.html")) # 클래스형 제네릭 뷰
]