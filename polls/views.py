from django.shortcuts import get_object_or_404, render
from polls.models import Question, Choice
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    lastest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list} # 딕셔너리 타입 객체로 탬플릿에 변수로 리턴
    return render(request, 'polls/index.html', context) # index.html을 불러와서 context 변수를 집어 넣고 HttpResponse객체를 반환 

def detail(request, question_id): # URL pattern에서 정규표현식으로 추출한 question_id 파라미터가 뷰 함수의 인자로 넘어옴
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question}) 

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # 숏컷을 사용하여 Question 모델 클래스부터 pk=question_pk를 검색 조건에 맞는 객체를 조회, 없으면 http404 익셉션 레이즈
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