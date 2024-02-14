FROM python:3.10.2
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV PIP_ROOT_USER_ACTION=ignore

COPY .. .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "[프로젝트 이름].wsgi:application"]