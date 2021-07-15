def interweave(s1, s2):
  s = ''
  for i in range(len(s2)):
    if not s1[i].isdigit(): s += s1[i]
    if not s2[i].isdigit(): s += s2[i]
  return s if len(s1) == 0 or s1[-1].isdigit() else s + s1[-1]

