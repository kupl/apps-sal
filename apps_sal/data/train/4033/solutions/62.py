def contamination(text, char):
  return ''.join([char for i in range(len(text))]) if text else ""
