def to_alternating_case(string):
   return ''.join([l.lower() if l == l.upper() else l.upper() for l in string])
