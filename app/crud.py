from .database import user_collection, meeting_collection
from .models import User, Meeting
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import pytz

async def create_user(user: User):
    user = user.dict()
    await user_collection.insert_one(user)

async def update_user(email: str, updates: dict):
    await user_collection.update_one({"email": email}, {"$set": updates})

async def create_meeting(meeting: Meeting):
    meeting = meeting.dict()
    await meeting_collection.insert_one(meeting)

async def get_meetings_in_range(start_time: datetime, end_time: datetime):
    if start_time.tzinfo is None or start_time.tzinfo.utcoffset(start_time) is None:
        start_time = pytz.utc.localize(start_time)
    if end_time.tzinfo is None or end_time.tzinfo.utcoffset(end_time) is None:
        end_time = pytz.utc.localize(end_time)

    booked_meetings = await meeting_collection.find({
        "meeting_start_time": {"$gte": start_time, "$lt": end_time},
        "meeting_end_time": {"$gte": start_time, "$lte": end_time}
    }).to_list(length=None)

    return booked_meetings



##neeed to work on this

    

    for meeting in booked_meetings:
        if meeting["meeting_start_time"].tzinfo is None or meeting["meeting_start_time"].tzinfo.utcoffset(meeting["meeting_start_time"]) is None:
            meeting_start_time = pytz.utc.localize(meeting["meeting_start_time"])
        else:
            meeting_start_time = meeting["meeting_start_time"]

        if meeting["meeting_end_time"].tzinfo is None or meeting["meeting_end_time"].tzinfo.utcoffset(meeting["meeting_end_time"]) is None:
            meeting_end_time = pytz.utc.localize(meeting["meeting_end_time"])
        else:
            meeting_end_time = meeting["meeting_end_time"]

        response["booked_meetings"].append({
            "start_time": meeting_start_time.isoformat(),
            "end_time": meeting_end_time.isoformat(),
            "timezone": meeting["timezone"],
            "meeting_type": meeting["meeting_type"]
        })

    return response