# AIDialogue sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/NazarDudiak/AI_Dialogue.git
$ cd AI_Dialogue
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ python -m virtualenv .venv
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

To test functionality, create an .evn file in the root of the project and add values for `SECRET_KEY`, `DB_NAME`, `DB_USER`, `DB_PASS`, `OPENAI_API_KEY`.
