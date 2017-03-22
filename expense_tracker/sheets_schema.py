import functools
import json
import jsonpickle
import sys

##############################################################################

class Base(object):
  def __init__(self, schema):
    for keyname in schema:
      typename = schema[keyname]

      if type(typename) is list:
        # Assumption is there is only one type in list
        typename = typename[0]
        method = functools.partial(self.append, keyname, typename)
        method_name = "append_" + keyname
      else:
        #method = lambda(value) : self.add(keyname, typename, value)
        method = functools.partial(self.add, keyname, typename)
        method_name = "add_" + keyname

      setattr(self, method_name, method)

  def __getstate__(self):
    state = {}
    for key, value in self.__dict__.items():
      if key.startswith('add_') or key.startswith('append_'):
        continue
      state[key] = value
    return state

  def __repr__(self):
    pickled_json = jsonpickle.encode(self, unpicklable=False)

    # HACK: Recreating object to get indentation
    obj_json = json.loads(pickled_json)
    str_json = json.dumps(obj_json, indent=4)

    return str_json

  def base_exit(self, message):
    print message
    sys.exit(1)

  def add(self, key, value_type, value):
    if value_type not in TYPE_DICT:
      err_msg = "Invalid type: " + value_type
      self.base_exit(err_msg)

    if type(value) is not TYPE_DICT[value_type]:
      err_msg = "Type mismatch. value=" + str(value) + " value_type=" +\
        str(value_type) + " type(value)=" + str(type(value))
      self.base_exit(err_msg)

    setattr(self, key, value)

  def append(self, key, value_type, value):
    if value_type not in TYPE_DICT:
      err_msg = "Invalid type: " + value_type
      self.base_exit(err_msg)

    if type(value) is not TYPE_DICT[value_type]:
      err_msg = "Type mismatch. value=" + str(value) + " value_type=" +\
        str(value_type) + " type(value)=" + str(type(value))
      self.base_exit(err_msg)

    if key not in self.__dict__:
      setattr(self, key, [])

    current_list = getattr(self, key)
    current_list.append(value)
    setattr(self, key, current_list)

##############################################################################

class ErrorValue(Base):
  def __init__(self):
    schema = {
      "type": "number",
      "message": "string",
    }
    super(ErrorValue, self).__init__(schema)

##############################################################################
 
class ExtendedValue(Base):
  def __init__(self):
    schema = {
      "numberValue": "number",
      "stringValue": "string",
      "boolValue": "boolean",
      "formulaValue": "string",
      "errorValue": "ErrorValue"
    }
    super(ExtendedValue, self).__init__(schema)

  """
  TODO: Figure this out
  def add(self, key, value_type, value):
    if len(self.__dict__) != 0:
      err_msg = "ExtendedValue is union. Already set:" + str(self.__dict__)
      self.base_exit(err_msg)
    
    super(ExtendedValue, self).add(key, value_type, value)
  """

##############################################################################

class CellData(Base):
  def __init__(self):
    schema = {
      "userEnteredValue": "ExtendedValue",
      "note": "string"
    }
    super(CellData, self).__init__(schema)

##############################################################################

class RowData(Base):
  def __init__(self):
    schema = {
      "values": ["CellData"]
    }
    super(RowData, self).__init__(schema)


##############################################################################

class GridData(Base):
  def __init__(self):
    schema = {
      "startRow": "number",
      "startColumn": "number",
      "rowData": ["RowData"]
    }
    super(GridData, self).__init__(schema)

##############################################################################

TYPE_DICT = {
  "number": int,
  "string": str,
  "boolean": bool,
  "ErrorValue": ErrorValue,
  "ExtendedValue": ExtendedValue,
  "CellData": CellData,
  "RowData": RowData
}
