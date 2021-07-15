def contamination(text, char):
  if len(text) == 0:
      return ""
  else:
      result = ""
      for c in text:
          result += char
      return result
