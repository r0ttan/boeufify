FROM kennethreitz/pipenv
ENV PORT '80'
COPY . /app
CMD python3 boeuf.py
EXPOSE 80
