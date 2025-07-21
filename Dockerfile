FROM python
WORKDIR /quizz
COPY . /quizz
CMD ["python3","quizz/py"]