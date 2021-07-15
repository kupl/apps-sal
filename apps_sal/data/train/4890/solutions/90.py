def find_difference(a, b):
      sum = 1
      sum1 = 1
      for i in a:
          sum = sum * i
      for j in b:
          sum1 = sum1 * j
      if sum - sum1 > 0:
          return sum - sum1
      else:
          return (sum - sum1) * -1
