def to_alternating_case(string):
   return string.swapcase() #''.join([l.lower() if l == l.upper() else l.upper() for l in string])
