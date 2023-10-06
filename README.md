# FastAPI Example App

## Accompanying Article


## Installation method 1 (Run application locally)

1. Clone this Repo

   `git clone (https://github.com/MetythornPenn/digital_map.git)`
2. Cd into the Fast-Api folder

   `cd server/src`
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

5. Install the required packages

   `pip install -r requirements.txt`
6. Start the app

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
