FROM python
COPY ./src /src
WORKDIR /src
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]