import json
import pprint
import unittest

from sheets_api import SheetsApi

TEST_DIR = "test"

class TestExpenseTracker(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    json_file = TEST_DIR + "/create_spreadsheet.json"
    json_data = open(json_file).read()

    spreadsheet_body = json.loads(json_data)
    cls._spreadsheet = SheetsApi().create_spreadsheet(spreadsheet_body)

  @classmethod
  def tearDownClass(cls):
    output = "Deleting of spreadsheet is NOT supported.\nManually Remove : " +\
             cls._spreadsheet["properties"]["title"]
    print output
  
  @unittest.skip("Ignoring this test")
  def test_create(self):
    json_file = TEST_DIR + "/create_spreadsheet.json"
    json_data = open(json_file).read()

    spreadsheet_body = json.loads(json_data)
    ret = SheetsApi().create_spreadsheet(spreadsheet_body)
    self.assertEqual(spreadsheet_body["properties"]["title"],
                     ret["properties"]["title"])

  """
  def test_read1(self):
    ret = SheetsApi().get_spreadsheet(self._spreadsheet["spreadsheetId"], [])

  def test_read2(self):
    ret = SheetsApi().get_spreadsheet(self._spreadsheet["spreadsheetId"], [])
  """

if __name__ == "__main__":
  unittest.main()
  print 
