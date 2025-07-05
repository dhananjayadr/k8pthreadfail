FROM python:3.9-slim
RUN pip install numpy
COPY pthread_test.py /pthread_test.py
CMD ["python", "/pthread_test.py"]
