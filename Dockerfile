FROM kennethreitz/pipenv
ENV PORT '80'
COPY . /app
CMD python3 mydish1_2.py
EXPOSE 80
