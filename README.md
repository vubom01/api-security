# API SECURITY
## Install and running app
```
$ git clone https://github.com/vubom01/my-event-app-be.git
$ cd my-event-app-be
$ virtualenv -p python3 .venv
$ source .venv/bin/activate (Ubuntu)
  .venv\Scripts\activate (Windows)
$ pip3 install -r requirements.txt
$ cp .env.example .env
$ uvicorn app.main:app --host 0.0.0.0 --port 5002 --reload
```