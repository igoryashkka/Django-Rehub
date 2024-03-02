FROM python:3.10.9

SHELL [ "/bin/bash","-c" ]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

RUN useradd -rms /bin/bash app && chmod 777 /opt /run

WORKDIR /app

RUN mkdir /app/static && mkdir /app/media && chown -R app:app /app && chmod 755 /app

COPY --chown=app:app . .

RUN pip install -r requirements.txt

USER app

CMD [ "gunicorn","-b","0.0.0.0:8001","base.wsgi:application"]