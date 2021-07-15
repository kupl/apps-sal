def resistor_parallel(*args):
    sum = 0
    for i in args:
      sum += 1/i
    return 1/sum

