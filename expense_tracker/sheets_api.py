from sheets_auth import get_service

class SheetsApi():
  def __init__(self):
    self._service = get_service()

  def create_spreadsheet(self, spreadsheet_body):
    request = self._service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    return response

  def get_spreadsheet(self, spreadsheet_id, ranges, include_grid_data=False):
    request =\
      self._service.spreadsheets().get(spreadsheetId=spreadsheet_id,
                                       ranges=ranges,
                                       includeGridData=include_grid_data)
    response = request.execute()
    return response

  def get_spreadsheet_values(self, spreadsheet_id, range_names):
    request  = self._service.spreadsheets().values().batchGet(
       spreadsheetId=spreadsheet_id, ranges=range_names)
    response = request.execute()
    return response
