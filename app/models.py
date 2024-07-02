from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr
    dnd_start_time: str
    dnd_end_time: str
    preferred_timezone: str

class Meeting(BaseModel):
    meeting_type: str
    meeting_start_time: datetime
    meeting_end_time: datetime
    timezone: str
    notification_interval: str
    participants: List[EmailStr]
