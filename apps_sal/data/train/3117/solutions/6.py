import re
def solve(s):
  return len(max(re.findall(r"[aeiou]+", s), key=len, default=""))
