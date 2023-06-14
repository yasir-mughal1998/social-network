# Social Network

#### Simple REST API-based Social Network in Django where Users can 
  - sign up 
  - create text post
  - view post
  - like post
  - unlike post

## Project Setup (How to run)
- Clone the repo
```
git clone https://github.com/yasir-mughal1998/social-network.git
```

- Create virtual environment using this command
```
python3 -m venv venv
```

- Activate the virtual environment
```
source venv/bin/activate
```
- Run the following command to install dependencies/libraries
```
pip install -r requirements.txt
```
- Run the migrations
```
python manage.py migrate
```
- Run the server using following command
```
python manage.py runserver
```
- Also run the celery on other terminal using following command
```
celery -A social_network worker -l info
```
#### Note:
- Make sure python and redis install in your system.
- Add .env file having environment variables in it to the project root level.


## To run application using docker, follow below approach

- Make sure docker and docker-compose installed in your system.
- Add docker.env file having environment variables in it to the project root level.
- Then run the following command
```
docker-compose up --build
```

## To run testcases, follow the below approach

- Add the following variable by running command in terminal
```
export DJANGO_SETTINGS_MODULE=social_network.settings
```
- Then Run command
```
pytest
```

## Swagger Url
 - http://127.0.0.1:8000/swagger/
