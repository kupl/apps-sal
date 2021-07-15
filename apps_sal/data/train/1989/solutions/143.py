class Solution:

  dbg = False

  def vis(self, s):
    result = \"\"
    for i in range(0,10):
      if s % 2 == 1:
        result = \"1\" + result
      else:
        result = \"0\" + result
      s = s >> 1
    return result

  def longestAwesome(self, s: str) -> int:
    good = set([0] + [1 << i for i in range(10)])

    state = 0
    states = [0]
    if self.dbg: print(\"9876543210\")
    for i, d in enumerate(s):
      state ^= 1 << (int(d))
      states.append(state)
      if self.dbg:
        print(self.vis(state))
    if self.dbg: print(\"9876543210\")

    seen = {0:0}

    best = 0
    for i, st_i in enumerate(states):
      for st_g in good:
        if st_i ^ st_g in seen:
          j = seen[st_i ^ st_g]
          length = i - j
          if length > best:
            best = length
      if st_i not in seen:
        seen[st_i] = i

    if self.dbg: print(best)
    return best

