def time_correct(t):
  if not t: return t
  try:
    h, m, s = [int(x) for x in t.split(':') if len(x) == 2]
    if s >= 60: s -= 60; m += 1
    if m >= 60: m -= 60; h += 1
    return f'{h%24:02}:{m:02}:{s:02}'
  except: pass
