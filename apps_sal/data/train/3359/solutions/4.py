from string import ascii_uppercase
def title_to_number(t):
  return 0 if len(t) == 0 else (ascii_uppercase.index(t[0]) + 1) * 26 ** (len(t) - 1) + title_to_number(t[1:])
