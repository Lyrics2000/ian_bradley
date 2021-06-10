# Ian Bradly Assignment

## Running the code
1. Install python on your machine (windos,linux,mac)
2. Open your cmd/bash/sh terminal of ur machine and run
   ```sh
    git clone https://github.com/Lyrics2000/ian_bradley.git
    cd ian_bradley
    

   ```
3. create a virtual env depending or you machine
   ```sh
   linux : python3 -m venv venv
   mac/windows : pip install virtualenv
   mac/windows : virtualenv venv

   ```
4. activating virtual environment
   ```sh
   linux/mac : source venv/bin/activate
   windows : source venv/Scripts/activate

   ```

5. install requirements.txt
   ```sh
   windows/mac/linux : pip install -r requirements.txt

   ```

6. running project
   ```sh
    windows/mac/linux : python manage.py runserver
   ```
7.  head over to http://localhost:8000/ to see the project
8.  for admin to change table contend head over to http://localhost:8000/admin username:admin password:1234