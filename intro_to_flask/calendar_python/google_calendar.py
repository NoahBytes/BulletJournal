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
""" 
def get_calendar_events():
    # Placeholder static events for testing
    return [
        {
            'summary': 'Test Event 1',
            'start': {'dateTime': '2024-10-10T10:00:00Z'},
            'description': 'This is a test event',
            'priority': 'High',
            'priority_class': 'high-priority'
        },
        {
            'summary': 'Test Event 2',
            'start': {'dateTime': '2024-10-11T11:00:00Z'},
            'description': 'This is another test event',
            'priority': 'Low',
            'priority_class': 'low-priority'
        }
    ]
    return render_template('calendar.html', events=events) """

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
