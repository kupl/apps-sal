def solve(s):
  uc, lc, num, sp = 0, 0, 0, 0
  for ch in s:
    if ch.isupper(): uc += 1
    elif ch.islower(): lc += 1
    elif ch.isdigit(): num += 1
    else: sp += 1
  return [uc, lc, num, sp]
