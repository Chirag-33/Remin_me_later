# Remin_me_later

This is a Django-based REST API for storing reminder messages. It accepts a datetime, a message, and a reminder type (SMS or Email). A JavaScript frontend is expected to send this data to the API.

## ✨ Features

- Accepts reminders via a POST API.
- Stores the message, reminder time, and type (email/sms) in a database.
- Built using Django and Django REST Framework.

##  How to Run (Using Pipenv)

1. **Install dependencies:**

   ```bash
   pipenv install
2. **ACtivate Environment:**
   pipenv shell
   
3. **API endpoint:**
http://127.0.0.1:8000/reminders/create/

I have tested the api but still if their is any problem that you are facing please let me know
