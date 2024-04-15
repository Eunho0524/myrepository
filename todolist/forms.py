from django import forms
from .models import Task

#사용자로부터 todolist 항목을 입력받는 form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
#입력 필드: 제목, 설명, 마감일
