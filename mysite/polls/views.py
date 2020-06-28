from django.shortcuts import get_object_or_404, render
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, TemplateView # 클래스형 / 제네릭 템플릭 상속

def index(request):
    lastest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list} # 딕셔너리 타입 객체로 탬플릿에 변수로 리턴
    return render(request, 'polls/index.html', context) # index.html을 불러와서 context 변수를 집어 넣고 HttpResponse객체를 반환 

def detail(request, question_id): # URL pattern에서 정규표현식으로 추출한 question_id 파라미터가 뷰 함수의 인자로 넘어옴
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # 숏컷을 사용하여 Question 모델 클래스부터 pk=question_id를 검색 조건에 맞는 객체를 조회, 없으면 http404 익셉션 레이즈
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # request.POST = html에서 제출된 form 을 담은 데이터 객체 . form에서 키가 choice에 해당하는 값
    except (KeyError, Choice.DoseNotExist): # 에러 발생시 detail.html으로 erorr_message와 question을 딕셔너리에 담아 전달
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
    # 결과 페이지로 리턴하기 위해 httpResponseRedirect를 리턴해준다. / reverse() = 패턴명으로 url 스트링을 가져옴 => url 하드코딩 방지

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

class MyView(View): # 클래스형 View를 상속받는다.
    def get(self, request):
        # code View rogic
        return HttpResponseRedirect('result')

class AboutView(TemplateView):
    template_name = "about.html" # TemplateView의 template_name 필드를 오버라이딩 한 것

# POST 처리 함수형과 클래스형의 비교
def myview(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            # cleand_date로 관련 로직 처리
            return HttpResponseRedirect('/success/')
    else:
        form = MyForm(initial={'key': 'value'})

    return render(request 'form_template.html', {'form': form})

class MyFormView(View):
    form_class = MyForm # 사용자에게 보여줄 폼을 정의한 forms.py 파일 내의 클래스명
    initial = {'key': 'value'}
    template_name = 'form_template.html' # 템플릿 이름

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid(): #유효한 폼 데이터로 처리할 로직코딩, super()함수를 사용하면 success_url로 지정된 URL로 리다이렉션 처리됨
            # cleand_data로 관련 로직 처리
            return HttpResponseRedirect('/success/')
            
        return render(request, self.template_name, {'form': form})
