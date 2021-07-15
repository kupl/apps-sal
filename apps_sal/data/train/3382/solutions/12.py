import re
def lowercase_count(str):
  return len(re.sub('[^a-z]', '', str))
