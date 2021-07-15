def super_pad(string, width, fill=" "):
  if not fill: return string
  needed = width - len(string)
    
  if fill[0] == ">":
      if needed < 0: return string[:needed]
      return string + (fill[1:] * needed)[:needed]
  elif fill[0] == "^":
      filler = fill[1:] * needed
      return (filler[:needed // 2 + needed % 2] + string + filler)[:width]
  else:
      if fill[0] == "<": fill = fill[1:]
      if needed < 0: return string[-needed:]
      return (fill * needed)[:needed] + string

