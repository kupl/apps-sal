def valid_parentheses(string):
  open_counter = 0 
  for i in string:
      if i=='(':         open_counter = open_counter + 1
      if i==')':         open_counter = open_counter - 1
      if open_counter<0: return False
  if open_counter==0:    return True
  return False
