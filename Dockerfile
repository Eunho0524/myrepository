# 베이스 이미지
FROM python:3.9

# 작업 디렉토리 설정
WORKDIR /todo

# 시스템 패키지 업데이트 및 의존성 설치
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc

# 파이썬 의존성 설치
COPY requirements.txt /todo/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . /todo/

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
