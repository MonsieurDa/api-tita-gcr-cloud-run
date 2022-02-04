# Some container that is already suitable for unicover
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# prevents python creating .pyc files #1 to enable
ENV PYTHONFAULTHANDLER=0 \ 
  # see logs (output) in real time
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip cache disbled
  PIP_NO_CACHE_DIR=off \
  # pip version checker
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  # timeout to install = 100 sec
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry no-interaction mode
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  # Versions:
  POETRY_VERSION=1.1.12

#define working directory
WORKDIR '/app/app'

# System deps:
# RUN pip install "poetry==$POETRY_VERSION"

# Generate requirements and install *all* dependencies.
COPY pyproject.toml poetry.lock ./
COPY ./test.py ./
COPY ./main.py ./
COPY ./model_weights/clf.bin ./model_weights/clf.bin

RUN pip install "poetry==$POETRY_VERSION" \
  && poetry export --dev --without-hashes --no-interaction --no-ansi -f requirements.txt -o requirements.txt \ 
  && pip install --force-reinstall --no-cache-dir -r requirements.txt \
  && python main.py

# run tests in dockerfile is not an good idea. For example run test in a githuB actions 
#or githab ci or travis before creating docker file
#RUN python -m test 
#RUN python main.py
CMD [ "main.py"]
