FROM python:3.9-slim  

WORKDIR /quizz  

COPY . .  

CMD ["python3", "quizz.py"]
