from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    preferred_timezone: str
    dnd_start_time: str
    dnd_end_time: str

class UserUpdate(BaseModel):
    preferred_timezone: Optional[str]
    dnd_start_time: Optional[str]
    dnd_end_time: Optional[str]

class MeetingCreate(BaseModel):
    meeting_type: str
    meeting_start_time: datetime
    meeting_end_time: datetime
    timezone: str
    notification_interval: str
    participants: List[EmailStr]

class FreeSlotsResponse(BaseModel):
    booked_meetings: List[MeetingCreate]
    free_slots: List[dict]
