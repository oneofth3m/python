import json
import pprint
import sys

from sheets_api import SheetsApi

def main():
  if len(sys.argv) != 2:
    print "Arguments : ", str(sys.argv)
    print "Usage: python create_spreadsheet.py sample.json"
    sys.exit(1)

  json_file = sys.argv[1]
  print "Creating Spreadsheet from ", json_file
  json_data = open(json_file).read()
  spreadsheet_body = json.loads(json_data)
  ret = SheetsApi().create_spreadsheet(spreadsheet_body)
  print ret

if __name__ == "__main__":
  main()
