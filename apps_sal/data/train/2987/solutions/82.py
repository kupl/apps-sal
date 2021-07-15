def is_divide_by(number, a, b):
  return (number%a==0 or a%number==0) and (number%b==0 or b%number==0)
