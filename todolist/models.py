from django.db import models

#할일 모듈 생성
#제목, 내용, 생성일, 마감일을 담을 수 있는 구조이다.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField() #내용을 입력할 수 있는 필드 
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

