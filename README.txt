##[How to Start the Application and API Collection]



##In Command Prompt:
(need to setup venv)

cd C:\Users\Aashi Pradhan\OneDrive\Desktop
cd Meetify


##it would look like this
C:\Users\Aashi Pradhan\OneDrive\Desktop\Meetify>.\venv\Scripts\activate

(venv) C:\Users\Aashi Pradhan\OneDrive\Desktop\Meetify>



##this is how the server will start:-


(venv) C:\Users\Aashi Pradhan\OneDrive\Desktop\Meetify>uvicorn app.main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\Aashi Pradhan\\OneDrive\\Desktop\\Meetify']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [6092] using StatReload
INFO:     Started server process [20348]
INFO:     Waiting for application startup.
INFO:     Application startup complete.


In POSTMAN ,we can trigger curls after setting up the server in command Prompt

API POSTMAN Collection

1. create new User

API : POST http://127.0.0.1:8000/users/

Request:

{
    "name": "Sashi Pradhan",
    "email": "sashi@gmail.com",
    "preferred_timezone": "IST",
    "dnd_start_time": "22:00",
    "dnd_end_time": "07:00"
}


Response:

{
    "message": "User created successfully"
}


Note : 500 for duplicate entry like if same user try to create account with same credentials





2.create new meeting

API: POST http://localhost:8000/meetings/

Request:

{
    "meeting_type": "online",
    "meeting_start_time": "2024-07-02T15:00:00Z",
    "meeting_end_time": "2024-07-02T16:00:00Z",
    "timezone": "UST",
    "notification_interval": "* * * * *",
    "participants": ["sachi@gmail.com"]
}

Response:

{
    "message": "Meeting created successfully"
}


3.update user details

API: PUT http://localhost:8000/users/sachi@gmail.com

Request:

{
    "preferred_timezone": "UST",
    "dnd_start_time": "21:00",
    "dnd_end_time": "06:00"
}


Response:

{
    "message": "User updated successfully"
}


4.get slots available

API : GET http://localhost:8000/meetings/free-slots/?start_time=2024-07-02T14:00:00Z&end_time=2024-07-02T18:00:00Z

Note : there is one offset error coming for this by resolving the datatype issue we can fix it due to time constraints ,couldnt work upon it.