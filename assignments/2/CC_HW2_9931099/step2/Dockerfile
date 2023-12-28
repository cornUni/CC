FROM python:3.10-slim

WORKDIR /app

COPY app.py requirements.txt /app/
COPY handlers/ /app/handlers/

RUN pip install --no-cache-dir -r requirements.txt

ENV API_KEY=5fadda87e2msh91fbec44114e41dp147ddejsn949782727d43
ENV EXPIRATION_TIME=300
ENV PORT=8080
ENV CITY=tehran

EXPOSE $PORT

CMD ["python", "app.py"]
