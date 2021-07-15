def contamination(text, char):
  l = 0
  if char == "":
      return ""
  elif text == "":
      return ""
  else:
      l = len(text)
      return char*l
