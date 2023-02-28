FROM python:3

COPY requirements.txt .
COPY main.py .
COPY calculate.py .
COPY constants.py .
COPY even_numbers.py .
COPY print_hello.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py"]

