def is_divide_by(number, a, b):
  return all([number%fac==0 for fac in (a,b)])
