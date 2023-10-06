# FastAPI Example App

![fastapi-0.92.0-informational](https://img.shields.io/badge/fastapi-0.92.0-informational) [![CodeQL](https://github.com/KenMwaura1/Fast-Api-example/actions/workflows/codeql.yml/badge.svg)](https://github.com/KenMwaura1/Fast-Api-example/actions/workflows/codeql.yml)
[![Docker Compose Actions Workflow](https://github.com/KenMwaura1/Fast-Api-example/actions/workflows/docker-image.yml/badge.svg)](https://github.com/KenMwaura1/Fast-Api-example/actions/workflows/docker-image.yml)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/kenmwaura1)
[![Twitter](https://badgen.net/badge/icon/twitter?icon=twitter&label=Follow&on)](https://twitter.com/Ken_Mwaura1)

This repository contains code for asynchronous example api using the [Fast Api framework](https://fastapi.tiangolo.com/) ,Uvicorn server and Postgres Database to perform crud operations on notes.

![Fast-api](images/fast-api-scrnsht.png)

## Accompanying Article

Read the full tutorial [here](https://dev.to/ken_mwaura1/getting-started-with-fast-api-and-docker-515)

## Installation method 1 (Run application locally)

1. Clone this Repo

   `git clone (https://github.com/KenMwaura1/Fast-Api-example)`
2. Cd into the Fast-Api folder

   `cd Fast-Api-example`
3. Create a virtual environment

   `python3 -m venv venv`
4. Activate virtualenv

   `source venv/bin/activate`

   For zsh users

   `source venv/bin/activate.zsh`

   For bash users

   `source venv/bin/activate.bash`

   For fish users

   `source venv/bin/activate.fish`
5. Cd into the src folder

   `cd src`
6. Install the required packages

   `python -m pip install -r requirements.txt`
7. Start the app

   ```shell
   python main.py
   ```

   7b. Start the app using Uvicorn

   ```shell
   uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8002
   ```

8. Ensure you have a Postgres Database running locally.
   Additionally create a `fast_api_dev` database with user `**fast_api**` having required privileges.
   OR
   Change the DATABASE_URL variable in the **.env** file inside then `app` folder to reflect database settings (user:password/db)

9. Check the app on [notes](http://localhost:8002/notes)
Open your browser and navigate to [docs](http://localhost:8002/docs) to view the swagger documentation for the api.