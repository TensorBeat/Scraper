FROM python:3.8

ENV POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1


RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY poetry.lock pyproject.toml poetry.toml ./
RUN poetry install --no-dev

COPY tensorbeat_scraper .

RUN ["poetry", "run", "main"]

