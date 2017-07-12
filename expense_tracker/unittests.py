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
    #cls._spreadsheet = SheetsApi().create_spreadsheet(spreadsheet_body)

  @classmethod
  def tearDownClass(cls):
    output = ""
    """
    output = "Deleting of spreadsheet is NOT supported.\nManually Remove : " +\
             cls._spreadsheet["properties"]["title"]
    """
    print output
  
  @unittest.skip("Ignoring this test")
  def test_create(self):
    json_file = TEST_DIR + "/create_spreadsheet.json"
    json_data = open(json_file).read()

    spreadsheet_body = json.loads(json_data)
    ret = SheetsApi().create_spreadsheet(spreadsheet_body)
    self.assertEqual(spreadsheet_body["properties"]["title"],
                     ret["properties"]["title"])

  @unittest.skip("Ignoring this test")
  def test_read_spreadsheet(self):
    ret = SheetsApi().get_spreadsheet(self._spreadsheet["spreadsheetId"], [])

  def test_read_values_via_spreadsheet(self):
    range = "Sheet1!A1:D2"
    ret = SheetsApi().get_spreadsheet(
        "1S52oEcqp6CcPr-Goo7Pkc1B401_QGVdxpth8wR5LTkM",
        range,
        True)
    import json
    str_json = json.dumps(ret, indent=2)
    print str_json

  def test_read_values(self):
    range = "Sheet1!A1:D5"
    ret = SheetsApi().get_spreadsheet_values(
        "1S52oEcqp6CcPr-Goo7Pkc1B401_QGVdxpth8wR5LTkM",
        range)
    import json
    str_json = json.dumps(ret, indent=2)
    print str_json

if __name__ == "__main__":
  unittest.main()
  print 
