def square_digits(n):
  return int("".join(str(pow(int(i), 2)) for i in str(n)))

