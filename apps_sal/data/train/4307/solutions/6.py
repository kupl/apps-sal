import string

def unused_digits(*args):
  #args is tuple of numbers
  #for each number we find, lets turn it into a string
  #then for each char in num str just add it to a set of found digits
  found_digits_chars = {char for n in args for char in str(n)}

  #let's say i have set of all digits {'0' to '9'}
  all_digits_chars = set(string.digits)
  #then just subtract found digits from set of all digits
  unused_digits_chars = all_digits_chars - found_digits_chars

  #then of course change format of answer to ordered strings
  return ''.join(sorted(list(unused_digits_chars)))

