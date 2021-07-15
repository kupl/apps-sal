def square_digits(num):
  return int(''.join([str(int(x)**2) for x in list(str(num))]))

