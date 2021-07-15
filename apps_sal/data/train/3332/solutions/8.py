import re
def autocorrect(input):
  return re.sub(r'(\bu\b|\byo[u]+\b)', "your sister", input, flags=re.IGNORECASE)

