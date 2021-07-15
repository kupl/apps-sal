def bowling_score(rolls):
  tot,i = 0,0
  for frm in range(10):
      fscr,i = rolls[i],i+1
      if fscr == 10:
          tot += fscr + rolls[i] + rolls[i+1]
          continue
      fscr += rolls[i]
      i += 1
      if fscr >= 10:
          tot += rolls[i]
      tot += fscr
  return tot

