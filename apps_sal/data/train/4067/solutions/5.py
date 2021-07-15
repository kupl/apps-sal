def iq_test(numbers):
  digits = [int(x) for x in numbers.split()]
  even = [x % 2 for x in digits]
  if sum(even) == 1:
    return even.index(1) + 1
  else:
    return even.index(0) + 1

