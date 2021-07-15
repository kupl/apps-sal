import re
def cards_and_pero(s):
  s = re.findall("...", s)
  if len(s) != len(set(s)):
      return ([-1, -1, -1, -1])
  else:
      P,K,H,T = 13,13,13,13
      for x in s:
          if x[0] == "P":
              P -= 1
          elif x[0] == "K":
              K -= 1
          elif x[0] == "H":
              H -= 1
          elif x[0] == "T":
              T -= 1
      return ([P, K, H, T])
