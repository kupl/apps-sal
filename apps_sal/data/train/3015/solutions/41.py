def get_issuer(number):
  s = str(number)
  l = len(s)
  if l == 15 and s[:2] in ('34', '37'): return 'AMEX'
  if l == 16 and s.startswith('6011'): return 'Discover'
  if l == 16 and 51 <= int(s[:2]) <= 55: return 'Mastercard'
  if l in (13,16) and s.startswith('4'): return 'VISA'
  return 'Unknown'

