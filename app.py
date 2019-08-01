from __future__ import print_function
import pickle
import os.path
import json
import base64
import connection
import dateutil.parser as parser
import MySQLdb
from MySQLdb import Error
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup

SCOPE = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
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
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPE)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().messages().list(userId='me').execute()
    messages = results.get('messages', [])

    if not messages:
        print('No messages found.')
    else:
        print('Messages:')

        finalList = []

        for message in messages:
            messageDictionary = {}
            message = service.users().messages().get(userId='me', id=message['id'], format='full').execute() # fetch the message using API
            messageId = message['id'] # getting the Id of an individual Message
            payload = message['payload'] # getting the Payload of the Message
            header = payload['headers'] # getting the Header of the Payload

            for one in header: # getting the Subject
              if one['name'] == 'Subject':
                messageSubject = one['value']
                messageDictionary['Subject'] = messageSubject
              else:
                pass

            try: # getting the Date
              if ['name'] == 'Date':
                unparsedDate = ['value']
                dateParsed = (parser.parse(unparsedDate))
                messageDate = (dateParsed.date())
                messageDictionary['Date'] = str(messageDate)
            except: # ignoring the ones that have weird timestamps
              pass

            for three in header: # getting the Sender
              if three['name'] == 'From':
                messageFrom = three['value']
                messageDictionary['Sender'] = messageFrom
              else:
                pass

            try: # fetching message Body
                messageParts = payload['parts'] # fetching the message Parts
                partOne = messageParts[0] # fetching First Element of the Part
                partBody = partOne['body'] # fetching Body of the Message
                partData = partBody['data'] # fetching Data from the Body
                dataString = str(partData) # converting to string the Data of the Body
                decodedBody = base64.urlsafe_b64decode(dataString) # decoding the Data String
                devopsBody = decodedBody.find('devops') # finding the DevOps word into the Data String
            except:
                pass

            if devopsBody >= 0: # when we get a message that contains the DevOps
                                # word it will give us a 0, if it doesn't a -1
                print(messageDictionary)
            else:
              pass

if __name__ == '__main__':
  main()