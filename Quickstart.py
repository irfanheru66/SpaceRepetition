from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.


    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    msg = input("Nama Materi: ")
    Deskripsi = input("Deskripsi (ex: bagian yang susah, atau objective materi ini): \n")

    start,end = generator()
    for i in range (len(start)):
        event = {
                        'summary': 'Space rep ke-{} materi {}'.format((i+1),msg),
                        'description': Deskripsi,
                        'start': {
                            'dateTime': start[i],
                            'timeZone': 'Asia/Jakarta',
                                },
                        'end': {
                            'dateTime': end[i],
                            'timeZone': 'Asia/Jakarta',
                            },
                }
        event = service.events().insert(calendarId='primary', body=event).execute()

    print("sucess")

def generator():
    delta = [3,10,40]
    start = []
    end = []

    for i in range(3):
        date = datetime.datetime.now().replace(microsecond=0,second=0,minute=0,hour=7) + datetime.timedelta(delta[i])
        start.append(date.isoformat())
        print(start[i])

        date = date + datetime.timedelta(hours=1)
        end.append(date.isoformat())
        print(end[i])
    
    return start,end




if __name__ == '__main__':
    main()