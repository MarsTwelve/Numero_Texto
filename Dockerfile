FROM python:3.11.7-alpine3.19
WORKDIR Numero_Texto
COPY num_to_text.py .
CMD ["python3", "num_to_text.py"]