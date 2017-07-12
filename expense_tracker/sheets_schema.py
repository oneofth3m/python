import functools
import json
import jsonpickle
import sys

from enum import Enum

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

# Done
class ErrorType:
  [
    ERROR_TYPE_UNSPECIFIED,
    ERROR,
    NULL_VALUE,
    DIVIDE_BY_ZERO,
    VALUE,
    REF,
    NAME,
    NUM,
    N_A,
    LOADING
  ] = range(10)

##############################################################################

# Done
class ErrorValue(Base):
  def __init__(self):
    schema = {
      "type": "number",  # enum(ErrorType)
      "message": "string"
    }
    super(ErrorValue, self).__init__(schema)

##############################################################################
 
# Done - Pending Union Check
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

# Done
class NumberFormatType:
  [
    NUMBER_FORMAT_TYPE_UNSPECIFIED,
    TEXT,
    NUMBER,
    PERCENT,
    CURRENCY,
    DATE,
    TIME,
    DATE_TIME,
    SCIENTIFIC
  ] = range(9)

##############################################################################

# Done
class NumberFormat:
    schema = {
      "type": "number",  # enum(NumberFormatType)
      "pattern": "string",
    }
    super(NumberFormat, self).__init__(schema)

##############################################################################

# Done
class Color:
    schema = {
      "red": "number",
      "green": "number",
      "blue": "number",
      "alpha": "number"
    }
    super(Color, self).__init__(schema)

##############################################################################

# Done
class Style:
  [
    STYLE_UNSPECIFIED,
    DOTTED,
    DASHED,
    SOLID,
    SOLID_MEDIUM,
    SOLID_THICK,
    NONE,
    DOUBLE
  ] = range(8)

##############################################################################

# Done
class Border:
    schema = {
      "style": "number", # enum(Style)
      "width": "number",
      "color": "Color"
    }
    super(Border, self).__init__(schema)

##############################################################################

# Done
class Borders:
    schema = {
      "top": "Border",
      "bottom": "Border",
      "left": "Border",
      "right": "Border",
    }
    super(Borders, self).__init__(schema)

##############################################################################

# Done
class Padding:
    schema = {
      "top": "number",
      "right": "number",
      "bottom": "number",
      "left": "number",
    }
    super(Padding, self).__init__(schema)

##############################################################################

# Done
class HorizontalAlign:
  [
    HORIZONTAL_ALIGN_UNSPECIFIED,
    LEFT,
    CENTER,
    RIGHT
  ] = range(4)

##############################################################################

# Done
class VerticalAlign:
  [
    VERTICAL_ALIGN_UNSPECIFIED,
    TOP,
    MIDDLE,
    BOTTOM
  ] = range(4)

##############################################################################

# Done
class WrapStrategy:
  [
    WRAP_STRATEGY_UNSPECIFIED,
    OVERFLOW_CELL,
    LEGACY_WRAP,
    CLIP,
    WRAP  
  ] = range(5)

##############################################################################

# Done
class TextDirection:
  [
    TEXT_DIRECTION_UNSPECIFIED,
    LEFT_TO_RIGHT,
    RIGHT_TO_LEFT
  ] = range(3)

##############################################################################

# Done
class TextFormat:
    schema = {
    "foregroundColor": "Color",
    "fontFamily": "string",
    "fontSize": "number",
    "bold": "boolean",
    "italic": "boolean",
    "strikethrough": "boolean",
    "underline": "boolean"
    }
    super(TextFormat, self).__init__(schema)

##############################################################################

# Done
class HyperlinkDisplayType:
  [
    HYPERLINK_DISPLAY_TYPE_UNSPECIFIED,
    LINKED,
    PLAIN_TEXT
  ] = range(3)

##############################################################################

# Done - Pending Union Check
class TextRotation:
    schema = {
      "angle": "number",
      "vertical": "boolean",
    }
    super(TextRotation, self).__init__(schema)

##############################################################################

# Done
class CellFormat:
    schema = {
      "numberFormat": "NumberFormat",
      "backgroundColor": "Color",
      "borders": "Borders",
      "padding": "Padding",
      "horizontalAlignment": "number", # enum(HorizontalAlign)
      "verticalAlignment": "number", # enum(VerticalAlign)
      "wrapStrategy": "number", # enum(WrapStrategy)
      "textDirection": "number", # enum(TextDirection)
      "textFormat": "TextFormat",
      "hyperlinkDisplayType": "number", # enum(HyperlinkDisplayType)
      "textRotation": "TextRotation"
    }
    super(CellFormat, self).__init__(schema)

##############################################################################

# Done
class TextFormatRun:
    schema = {
      "startIndex": "number",
      "format": "TextFormat"
    }
    super(TextFormatRun, self).__init__(schema)

##############################################################################

# Done
class ConditionType:
  [
    CONDITION_TYPE_UNSPECIFIED,
    NUMBER_GREATER,
    NUMBER_GREATER_THAN_EQ,
    NUMBER_LESS,
    NUMBER_LESS_THAN_EQ,
    NUMBER_EQ,
    NUMBER_NOT_EQ,
    NUMBER_BETWEEN,
    NUMBER_NOT_BETWEEN,
    TEXT_CONTAINS,
    TEXT_NOT_CONTAINS,
    TEXT_STARTS_WITH,
    TEXT_ENDS_WITH,
    TEXT_EQ,
    TEXT_IS_EMAIL,
    TEXT_IS_URL,
    DATE_EQ,
    DATE_BEFORE,
    DATE_AFTER,
    DATE_ON_OR_BEFORE,
    DATE_ON_OR_AFTER,
    DATE_BETWEEN,
    DATE_NOT_BETWEEN,
    DATE_IS_VALID,
    ONE_OF_RANGE,
    ONE_OF_LIST,
    BLANK,
    NOT_BLANK,
    CUSTOM_FORMULA
  ] = range(29)

##############################################################################

# Done
class RelativeDate:
  [
    RELATIVE_DATE_UNSPECIFIED,
    PAST_YEAR,
    PAST_MONTH,
    PAST_WEEK,
    YESTERDAY,
    TODAY,
    TOMORROW
  ] = range(7)

##############################################################################

# Done - Pending Union Check
class ConditionValue:
    schema = {
      "relativeDate": "number", # enum(RelativeDate)
      "userEnteredValue": "string"
    }
    super(ConditionValue, self).__init__(schema)

##############################################################################

# Done
class BooleanCondition:
    schema = {
      "type": "number", # enum(ConditionType)
      "values": ["ConditionValue"]
    }
    super(BooleanCondition, self).__init__(schema)

##############################################################################

# Done
class DataValidationRule:
    schema = {
      "condition": "BooleanCondition",
      "inputMessage": "string",
      "strict": "boolean",
      "showCustomUi": "boolean"
    }
    super(DataValidataionRule, self).__init__(schema)

##############################################################################

# Done
class GridRange:
    schema = {
      "sheetId": "number",
      "startRowIndex": "number",
      "endRowIndex": "number",
      "startColumnIndex": "number",
      "endColumnIndex": "number"
    }
    super(GridRange, self).__init__(schema)

##############################################################################

class PivotGroup:
    schema = {
    }
    super(PivotGroup, self).__init__(schema)

##############################################################################

class PivotValue:
    schema = {
    }
    super(PivotValue, self).__init__(schema)

##############################################################################

class PivotValueLayout:
  [
  ] = range(3)

##############################################################################

# "criteria" unimplemented. Its a map?
class PivotTable:
    schema = {
      "source": "GridRange",
      "rows": ["PivotGroup"],
      "columns": ["PivotGroup"],
      """
      "criteria": {
         string: {
           object(PivotFilterCriteria)
         },
         ...
      },
      """
      "values": ["PivotValue"],
      "valueLayout": "number" # enum(PivotValueLayout)
    }
    super(PivotTable, self).__init__(schema)

##############################################################################

# Done
class CellData(Base):
  def __init__(self):
    schema = {
      "userEnteredValue": "ExtendedValue",
      "effectiveValue": "ExtendedValue",
      "formattedValue": "string",
      "userEnteredFormat": "CellFormat",
      "effectiveFormat": "CellFormat",
      "hyperlink": "string",
      "note": "string",
      "textFormatRuns": ["TextFormatRun"],
      "dataValidation": "DataValidationRule",
      "pivotTable": "PivotTable"
    }
    super(CellData, self).__init__(schema)

##############################################################################

# Done
class RowData(Base):
  def __init__(self):
    schema = {
      "values": ["CellData"]
    }
    super(RowData, self).__init__(schema)


##############################################################################

# Done
class DimensionProperties(Base):
  def __init__(self):
    schema = {
      "hiddenByFilter": "boolean",
      "hiddenByUser": "boolean",
      "pixelSize": "number"
    }
    super(DimensionProperties, self).__init__(schema)


##############################################################################

# Done
class GridData(Base):
  def __init__(self):
    schema = {
      "startRow": "number",
      "startColumn": "number",
      "rowData": ["RowData"]
      "rowMetadata": ["DimensionProperties"],
      "columnMetadata": ["DimensionProperties"]
    }
    super(GridData, self).__init__(schema)

##############################################################################

TYPE_DICT = {
  "number": int,
  "string": str,
  "boolean": bool,
  "ErrorValue": ErrorValue,
  "ExtendedValue": ExtendedValue,
  "NumberFormat": NumberFormat,
  "Color": Color,
  "Border": Border,
  "Borders": Borders,
  "Padding": Padding,
  "TextFormat": TextFormat,
  "TextRotation": TextRotation,
  "CellFormat": CellFormat,
  "TextFormatRun": TextFormatRun,
  "ConditionValue": ConditionValue,
  "BooleanCondition": BooleanCondition,
  "DataValidationRule": DataValidationRule,
  "GridRange": GridRange,
  "PivotGroup": PivotGroup,
  "PivotValue": PivotValue,
  "PivotTable": PivotTable,
  "CellData": CellData,
  "RowData": RowData,
  "DimensionProperties": DimensionProperties,
  "GridData": GridData
}
