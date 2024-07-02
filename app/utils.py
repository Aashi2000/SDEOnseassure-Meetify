from datetime import datetime, timedelta, timezone
import pytz

def get_free_slots(meetings, start_time, end_time):
    free_slots = []
    current_time = start_time.replace(tzinfo=None) 

    for meeting in meetings:
        if isinstance(meeting["meeting_start_time"], str):
            meeting_start_time = datetime.fromisoformat(meeting["meeting_start_time"])
        else:
            meeting_start_time = meeting["meeting_start_time"]

        if isinstance(meeting["meeting_end_time"], str):
            meeting_end_time = datetime.fromisoformat(meeting["meeting_end_time"])
        else:
            meeting_end_time = meeting["meeting_end_time"]

        if meeting_start_time.tzinfo is None or meeting_start_time.tzinfo.utcoffset(meeting_start_time) is None:
            meeting_start_time = pytz.utc.localize(meeting_start_time)
        if meeting_end_time.tzinfo is None or meeting_end_time.tzinfo.utcoffset(meeting_end_time) is None:
            meeting_end_time = pytz.utc.localize(meeting_end_time)

        if current_time < meeting_start_time.replace(tzinfo=None): 
            free_slots.append({
                "start_time": current_time,
                "end_time": meeting_start_time,
                "duration": int((meeting_start_time - current_time).total_seconds() / 60)
            })

        current_time = max(current_time, meeting_end_time.replace(tzinfo=None))  # Convert to naive datetime

    if current_time < end_time.replace(tzinfo=None):  # Convert to naive datetime
        free_slots.append({
            "start_time": current_time,
            "end_time": end_time,
            "duration": int((end_time - current_time).total_seconds() / 60)
        })

    return free_slots
