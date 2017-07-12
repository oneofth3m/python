from sheets_schema import *

g = GridData()
g.add_startRow(0)
g.add_startColumn(0)
# 
r = RowData()
## 
c = CellData()
e = ExtendedValue()
e.add_numberValue(10)
c.add_userEnteredValue(e)
c.add_note("Note 1")
## 
r.append_values(c)
## 
c = CellData()
e = ExtendedValue()
e.add_stringValue("Peace")
c.add_userEnteredValue(e)
c.add_note("Note 2")
## 
r.append_values(c)
# 
g.append_rowData(r)
# 
r = RowData()
## 
c = CellData()
e = ExtendedValue()
e.add_numberValue(100)
c.add_userEnteredValue(e)
c.add_note("Note 3")
## 
r.append_values(c)
# 
g.append_rowData(r)
# 
r = RowData()
## 
c = CellData()
e = ExtendedValue()
e.add_numberValue(101)
c.add_userEnteredValue(e)
c.add_note("Note 4")
## 
r.append_values(c)
## 
c = CellData()
e = ExtendedValue()
e.add_stringValue("War")
c.add_userEnteredValue(e)
c.add_note("Note 5")
## 
r.append_values(c)
#
g.append_rowData(r)

print g

