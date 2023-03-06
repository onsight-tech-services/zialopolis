FROM python:3.11.2

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install 