import re
yes = "In with a chance"
no = "Plenty more fish in the sea"
def validate_number(string):
  return yes if re.match(r'^(\+44|0)7[\d]{9}$',re.sub('-','',string)) else no
