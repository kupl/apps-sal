def single_digit(n):
  return n if n<10 else single_digit(bin(n).count("1"))
