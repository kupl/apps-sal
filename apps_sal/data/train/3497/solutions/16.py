def isPP(num):
    for n in range(2, 100):
        if abs( num ** (1/n) - round(num ** (1/n))) < 0.0000001:
          return [round(num ** (1/n)), n]
        n += 1
