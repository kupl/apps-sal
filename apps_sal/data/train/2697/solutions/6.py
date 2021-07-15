def solution(s):
  res = ""
  letters = [char for char in s]
  print(letters)
  for i in range(len(letters)):
    if(letters[i] == letters[i].upper()):
      res+=" "+letters[i]
    else:
      res+=letters[i]
  return res
