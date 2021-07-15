def solution(string):
    if len(string) == 5:
      return string[4] + string[3] + string[2] + string[1] + string[0]
    if len(string) == 4:
      return string[3] + string[2] + string[1] + string[0]
    if len(string) == 3:
      return string[2] + string[1] + string[0]
    if len(string) == 2:
      return string[1] + string[0]
    if len(string) == 1:
      return string[0]
    if len(string) == 0:
      return ""
    pass
