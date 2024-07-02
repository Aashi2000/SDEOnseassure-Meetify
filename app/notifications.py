import requests
from .database import user_collection
from datetime import datetime, time
import pytz

async def send_notification(user_email: str, message: str):
    try:
        user = await user_collection.find_one({"email": user_email})
        
        if not user:
            print(f"User with email '{user_email}' not found.")
            return
        
        preferred_timezone = user.get("preferred_timezone", None)
        
        if not preferred_timezone:
            print(f"Preferred timezone not found for user '{user_email}'.")
            return
        
        if preferred_timezone == "IST":
            # Handle IST specifically
            timezone_obj = pytz.timezone("Asia/Kolkata")
        else:
            try:
                timezone_obj = pytz.timezone(preferred_timezone)
            except pytz.UnknownTimeZoneError:
                print(f"Unknown timezone: '{preferred_timezone}'.")
                return
        
        now = datetime.now(timezone_obj).time()
        dnd_start = datetime.strptime(user["dnd_start_time"], "%H:%M").time()
        dnd_end = datetime.strptime(user["dnd_end_time"], "%H:%M").time()

        if not (dnd_start <= now <= dnd_end):
            webhook_url = "https://webhook.site/63524c72-fe2f-42ca-9f9e-f357dff15397"
            requests.post(webhook_url, json={"message": message})
            print(f"Notification sent to {user_email}: {message}")
        else:
            print(f"User is in Do Not Disturb period: {user_email}")
    
    except Exception as e:
        print(f"Error occurred while processing notification for {user_email}: {str(e)}")
