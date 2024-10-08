import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GOOGLE_CALENDAR_API_KEY')
CALENDAR_ID = 'd497c4745910aab442b400aeb60f236d70e031adc037ac8ca40e31dec673e839@group.calendar.google.com' 

# Google Calendar API URL to fetch events
url = f'https://www.googleapis.com/calendar/v3/calendars/{CALENDAR_ID}/events?key={API_KEY}'

def get_calendar_events():
    response = requests.get(url)
    if response.status_code == 200:
        events = response.json().get('items', [])
        return events
    else:
        print(f"Error fetching events: {response.status_code}, {response.json()}")
        return [] 


def display_events(events):
    if not events:
        print("No upcoming events found.")
    else:
        for event in events:
            event_summary = event.get('summary', 'No title')
            start_time = event['start'].get('dateTime', event['start'].get('date', 'No start time'))
            print(f"Event: {event_summary}, Start: {start_time}")

if __name__ == "__main__":
    events = get_calendar_events()
    display_events(events)
