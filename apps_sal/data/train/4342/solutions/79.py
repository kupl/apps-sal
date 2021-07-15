def no_space(x):
  array = x.split(' ')
  for whitespace in array:
    if whitespace == '':
      array.remove(whitespace)
  a_string = ''.join(array)
  return a_string
