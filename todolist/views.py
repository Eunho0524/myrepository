from django.shortcuts import render, redirect, get_object_or_404
#앞에서 만든 task 모델을 불러온다
from todolist.models import Task
#taskform은 todolist 항목을 입력받는 form이다.
from .forms import TaskForm 
from django.contrib import messages

#todolist를 보여줄 수 있는 뷰
def todo_list(request):

    # 세션에 삭제 메시지가 있으면 보여준 후 삭제
    if 'delete_success' in request.session:
        messages.success(request, request.session.pop('delete_success'))

    # 모든 Todo 아이템을 가져와 tasks 변수에 저장
    tasks = Task.objects.all()
    # todo_list.html 템플릿에 tasks를 전달하여 렌더링
    return render(request, 'todolist/todo_list.html', {'tasks': tasks})

#todolist 상세 설명을 볼 수 있는 뷰 
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todolist/task_detail.html', {'task': task})

#todolist의 항목을 추가할 수 있는 뷰
def add_task(request):
    # HTTP POST 요청
    if request.method == 'POST':
        # 입력한 데이터를 기반으로 TaskForm을 생성
        form = TaskForm(request.POST)
        # 폼이 유효한지 확인
        if form.is_valid():
            form.save()
            messages.success(request, '할 일이 추가되었습니다.')
            return redirect('todo_list')
    else:
        # HTTP GET 요청일 때, 빈 폼을 생성
        form = TaskForm()
    # add_task.html 템플릿에 폼을 전달하여 렌더링
    return render(request, 'todolist/add_task.html', {'form': form})


#기존 todolist의 항목을 수정할 수 있는 뷰 
def edit_task(request, pk):
    # pk에 해당하는 Task 객체를 가져온다. 
    # 혹시 없으면 404 에러를 반환
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # HTTP POST 요청일 때, 기존의 Task 객체를 폼에 채워넣는다.
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
           form.save()
           messages.success(request, '할 일이 수정되었습니다.')
           return redirect('todo_list')
    else:
        form = TaskForm(instance=task)
    # edit_task.html 템플릿에 폼과 task를 전달하여 렌더링
    return render(request, 'todolist/edit_task.html', {'form': form})

# 기존 todolist 항목을 삭제할 수 있는 뷰 
def delete_task(request, pk):
    #pk에 해당하는 task객체 가져오기
    #혹시 없으면 404에러 반환
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, '할 일이 삭제되었습니다.')
        
        # 네임스페이스를 사용하여 리디렉션
        return redirect('todo_list')
   # confirm_delete.html 템플릿에 task를 전달하여 렌더링
    return render(request, 'todolist/confirm_delete.html', {'task': task})