def unique_digit_products(a):
  return len(set(eval('*'.join(str(x))) for x in a))
