FROM python:3.8 as dev

# install poetry
ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="$POETRY_HOME/bin:$PATH"


FROM dev

WORKDIR /app

# Install dependencies
COPY poetry.lock pyproject.toml poetry.toml ./
RUN poetry install --no-dev

#Copy over prod files
COPY gcp-admin-key.json .env ./
COPY /tensorbeat_scraper ./tensorbeat_scraper
RUN poetry install --no-dev

CMD ["poetry", "run", "main"]

