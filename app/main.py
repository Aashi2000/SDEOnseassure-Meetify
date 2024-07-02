from fastapi import FastAPI, HTTPException, Depends
from .schemas import UserCreate, UserUpdate, MeetingCreate, FreeSlotsResponse
from .crud import create_user, update_user, create_meeting, get_meetings_in_range
from .notifications import send_notification
from .utils import get_free_slots
from datetime import datetime

app = FastAPI()

@app.post("/users/")
async def create_new_user(user: UserCreate):
    await create_user(user)
    return {"message": "User created successfully"}

@app.put("/users/{email}")
async def update_user_details(email: str, user: UserUpdate):
    await update_user(email, user.dict(exclude_unset=True))
    return {"message": "User updated successfully"}

@app.post("/meetings/")
async def create_new_meeting(meeting: MeetingCreate):
    await create_meeting(meeting)
    for participant in meeting.participants:
        await send_notification(participant, "You have a new meeting")
    return {"message": "Meeting created successfully"}

@app.get("/meetings/free-slots/", response_model=FreeSlotsResponse)
async def get_free_time_slots(start_time: datetime, end_time: datetime):
    meetings = await get_meetings_in_range(start_time, end_time)
    free_slots = get_free_slots(meetings, start_time, end_time)
    return {
        "booked_meetings": meetings,
        "free_slots": free_slots
    }
