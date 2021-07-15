import re
def get_textliterals(pv_code):
  print(pv_code)
  result = [(match.start(1), match.end(1)) for match in re.finditer(r"(?:--[^\n]*\n?|/\*.*?\*/|((?:'[^']*')+|'[^']*$)|.)", pv_code, re.MULTILINE) if match.group(1)]
  return result

