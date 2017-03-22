import json
import jsonpickle

class Base:
  def __repr__(self):
    pickled = jsonpickle.encode(self, unpicklable=False)
    json_obj = json.loads(pickled)
    return json.dumps(json_obj, indent=2)

class ExtendedValue(Base):
  def __init__(self, type, value):
    if type == "number":
      self.numberValue = value
    elif type == "string":
      self.stringValue = value

class CellData(Base):
  def __init__(self,
               userEnteredValue,
               note=None):
    self.userEnteredValue = userEnteredValue
    self.note = note

class RowData(Base):
  def __init__(self, values):
    self.values = []

  def add_CellData(self, CellData):
    self.values.append(CellData)

if __name__ == "__main__":
  userEnteredValue_1 = ExtendedValue("number", 10)
  note_1 = "Note 1"
  cellData_1 = CellData(userEnteredValue_1, note_1)

  userEnteredValue_2 = ExtendedValue("number", 20)
  note_2 = "Note 2"
  cellData_2 = CellData(userEnteredValue_2)

  rowData_1 = RowData([])
  rowData_1.add_CellData(cellData_1)
  rowData_1.add_CellData(cellData_2)
  
  print rowData_1



