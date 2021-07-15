import re
def Dragon(n):
  if not isinstance(n, int) or n < 0: return ''
  sub_table = { 'a' : 'aRbFR', 'b' : 'LFaLb' }
  s = 'Fa'
  for i in range(0, n):
    s = re.sub(r'[ab]', lambda m: sub_table[m.group()], s)
  return s.translate(None, 'ab')

