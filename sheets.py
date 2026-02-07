from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
CREDS = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)

SPREADSHEET_ID = "YOUR_SHEET_ID"

def log_task(data):
    service = build("sheets", "v4", credentials=CREDS)
    sheet = service.spreadsheets()

    values = [[data["Customer Name"], data["Topic"], data["Urgency"], data["Summary"]]]

    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range="Sheet1!A:D",
        valueInputOption="RAW",
        body={"values": values}
    ).execute()
