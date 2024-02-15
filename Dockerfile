FROM python:3.11.7-alpine3.19
WORKDIR /Numero_Texto
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "num_to_txt_API:app", "--host", "0.0.0.0", "--port", "8080"]