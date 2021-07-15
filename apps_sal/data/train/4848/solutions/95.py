def char_freq(message):
    d = {}
    for s in message:
      if s not in d:
        d[s] = 1
      else:
        d[s] = d[s] + 1
    return d
