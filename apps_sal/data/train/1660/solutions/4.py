def simplify(poly):
  import re
  from collections import defaultdict
  
  terms = defaultdict(lambda: 0)
  m = re.finditer(r'([+-]?)\s*(\d?)(\w+)', poly)

  for x in m:
    terms[frozenset(x.group(3))] += int(x.group(1) + x.group(2)) if x.group(2) else -1 if x.group(1) == '-' else 1

  f = [('+' if sign == 1 else '-' if sign==-1 else '{:+d}'.format(sign), ''.join(sorted(term))) for term, sign in terms.items() if sign != 0]
  
  ff = sorted(f, key=lambda x: (len(x[1]), x[1]))
  
  first_term = (ff[0][0][1:] if ff[0][0][0] == '+' else ff[0][0]) + ff[0][1]
  
  return first_term + ''.join(p + t for p, t in ff[1:])
