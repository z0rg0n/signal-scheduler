import schedule
import time
import subprocess
from datetime import datetime
import pytz



def send_signal_message(identifier, message, is_group):
    try:
        if is_group:
            subprocess.run([
                'signal-cli',
                '-u', '+123456789',  # Replace with your Signal phone number
                'send',
                '-g', identifier,
                '-m', message
            ], check=True)
            print(f"Message sent to group {identifier} at {datetime.now()}")
        else:
            subprocess.run([
                'signal-cli',
                '-u', '+123456789',  # Replace with your Signal phone number
                'send',
                '-m', message,
                identifier
            ], check=True)
            print(f"Message sent to {identifier} at {datetime.now()}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to send message to {identifier}: {e}")

def schedule_message(date_time, identifier, message, timezone='Asia/Tokyo', is_group=False):
    local_tz = pytz.timezone(timezone)
    schedule_time = local_tz.localize(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S'))
    now = datetime.now(local_tz)
    delay = (schedule_time - now).total_seconds()

    if delay > 0:
        schedule_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').time()
        schedule.every().day.at(schedule_time.strftime("%H:%M:%S")).do(send_signal_message, identifier, message, is_group)
        print(f"Scheduled message to {'group' if is_group else 'recipient'} {identifier} at {date_time} {timezone}")
    else:
        print(f"Time {date_time} {timezone} is in the past, cannot schedule message.")

# Replace these IDs with actual IDs
self = '+123456789'

group1 = '123456789abcdefgABCDEFG'
group2 = '123456789abcdefgABCDEFG'

person1 = '+1111111111'
person2 = '+222222222'

scheduled_messages = [
    {'date_time': '2024-07-04 00:00:01', 'identifier': group1, 'message': 'This is a group message 🤖', 'timezone': 'America/New_York', 'is_group': True},
    {'date_time': '2025-05-11 00:00:01', 'identifier': person1, 'message': 'I made a robot so I don\'t have to remember your birthday.', 'timezone': 'Asia/Tokyo', 'is_group': False},
    {'date_time': '2025-06-17 00:01:00', 'identifier': person2, 'message': 'Good morning birthday human🤖', 'timezone': 'America/New_York', 'is_group': False},
    {'date_time': '2025-07-11 18:41:01', 'identifier': self, 'message': 'Don\'t forget to submit your timecard', 'timezone': 'Asia/Tokyo', 'is_group': True},
    # Add more scheduled messages as needed
]

for msg in scheduled_messages:
    schedule_message(msg['date_time'], msg['identifier'], msg['message'], msg['timezone'], msg['is_group'])

while True:
    schedule.run_pending()
    time.sleep(1)
