# syntax=docker/dockerfile:1
FROM python:3.11

WORKDIR JobFinderAPI

COPY . JobFinderAPI

RUN apt update
RUN apt upgrade

RUN yes | apt install -f ./JobFinderAPI/config/chrome411.deb

EXPOSE 8000

RUN pip install -r Job*/config/requirements.txt

CMD ["python", "JobFinderAPI/Py/JobFinder.py"]

