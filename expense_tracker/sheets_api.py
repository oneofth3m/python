from sheets_auth import get_service

class SheetsApi():
  def __init__(self):
    self._service = get_service()

  def create_spreadsheet(self, spreadsheet_body):
    request = self._service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    return response

  def get_spreadsheet(self, spreadsheet_id, ranges):
    request = self._service.spreadsheets().get(spreadsheetId=spreadsheet_id,
                                               ranges=ranges)
    response = request.execute()
    return response

