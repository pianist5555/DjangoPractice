from mysite.polls.models import Question, Choice
from django.utils import timezone

# Create
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save() 

# Read 
Question.objects.all() # Queryset collection 반환
Question.objects.filter( # 해당 조건은 포함
    question_text_startswith='What'
    ).exclude( # 해당 조건은 제외
    pub_date_gte=datetime.date.today()
    ).filter(
    pub_date_gte=datetime.date.today(2005, 1, 30)
    )
Question.objects.get(pk=1) # 한 개의 요소만 있는 것이 확실한 경우 한 개의 객체를 가져온다. Queryset collection(X)
Question.objects.all()[:5] # list 반환 Queryset collection(X) 갯수 제한을 해서 가져온다.
Question.objects.all()[5:10]
Question.objects.all()[5:]

# Update
q.question_text = 'What is your favorite hoobby?' 
q.save()
Question.objects.filter(pub_date_year=2007).update(question_text='Evrything is the same') # 여러 객체 Update

# Delete
Question.objects.filter(pub_date_year=2005).delete()
Question.objects.all().delete() # 전체삭제