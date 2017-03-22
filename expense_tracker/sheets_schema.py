import functools
import json
import jsonpickle
import sys

##############################################################################

class Base(object):
  def __init__(self, schema):
    for keyname in schema:
      typename = schema[keyname]
      #add_method = lambda(value) : self.add_key_value(keyname, typename, value)
      add_method = functools.partial(self.add_key_value, keyname, typename)
      add_method_name = "add_" + keyname
      setattr(self, add_method_name, add_method)

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

  def add_key_value(self, key, value_type, value):
    if value_type not in TYPE_DICT:
      err_msg = "Invalid type: " + value_type
      self.base_exit(err_msg)

    if type(value) is not TYPE_DICT[value_type]:
      err_msg = "Type mismatch. value=" + str(value) + " value_type=" +\
        str(value_type) + " type(value)=" + str(type(value))
      self.base_exit(err_msg)

    setattr(self, key, value)

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
  def add_key_value(self, key, value_type, value):
    if len(self.__dict__) != 0:
      err_msg = "ExtendedValue is union. Already set:" + str(self.__dict__)
      self.base_exit(err_msg)
    
    super(ExtendedValue, self).add_key_value(key, value_type, value)
  """

##############################################################################

TYPE_DICT = {
  "number": int,
  "string": str,
  "boolean": bool,
  "ErrorValue": ErrorValue,
  "ExtendedValue": ExtendedValue
}
