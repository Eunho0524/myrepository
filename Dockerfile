# 베이스 이미지 설정
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /todo

# 필요한 파일 복사
COPY requirements.txt .
#requirments.txt 파일에는 애플리케이션이 실행되기 위해 
#필요한 PYTHON 패키지들의 목록이 담겨 있다. 

#종속성 설치
RUN pip install -r requirements.txt 

# 소스 코드 복사
COPY . .

#Django 애플리케이션 실행 명령 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]