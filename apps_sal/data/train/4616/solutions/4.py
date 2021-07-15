def single_digit(n):
    return n  if n < 10 else single_digit(sum(  int(d) for d in  bin(n)[2:]))
