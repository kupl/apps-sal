def close_compare(a, b, margin=0):
  # If the absolute value of their difference is no greater than the margin,
  # then they're equal enough.
  if abs(a - b) <= margin:
    return 0;
    
  # They removed the cmp() function in Python 3, so we use this weird-looking expression
  # instead.  This works because arithmetic operations like '-' coerce their operands into
  # numbers.  A boolean operand is coerced into a 1 if it's True or a 0 if it's False.
  # So if a > b, then this expression is equivalent to True - False, which after coercion
  # becomes 1 - 0, which is 1.  Likewise, if a < b, then it's 0 - 1, which is -1.  And if
  # a == b, then it's False - False, which coerces to 0 - 0, which is 0.
  return (a > b) - (a < b)
