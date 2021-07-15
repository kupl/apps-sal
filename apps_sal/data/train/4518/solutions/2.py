from re import search
def wheres_wally(s):
  match = search(r'(?:^|\s)Wally(?:\W|$)', s)
  return -1 if match == None else match.start(0) + 1 if match.group(0)[0].isspace() else match.start(0)

