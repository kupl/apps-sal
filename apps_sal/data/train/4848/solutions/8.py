def char_freq(message):
  chars, counts = list(), list()
  for c in message:
    if c not in chars:
      chars.append(c)
      counts.append(message.count(c))
  return dict(zip(chars, counts))
