def get_char(c):
  # Your code goes here ^_^
  if c < 0 or c > 255:
      print('ASCII out of range')
      return -1      
  return chr(c)
