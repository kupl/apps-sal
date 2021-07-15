import math
def sillycase(s):
  return s[:int(math.ceil(len(s)/2.0))].lower() + s[int(math.ceil(len(s)/2.0)):].upper()
