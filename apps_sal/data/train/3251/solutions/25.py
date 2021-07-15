def primeFactors(n):
    i = 2
    j = 0
    out = ''
    while n > 1:
      if n % i == 0:
          n //= i
          j += 1
      else:
          if j == 1:
              out += '({})'.format(i)
          elif j > 1:
              out += '({}**{})'.format(i, j)
          i += 1
          j = 0
    return out + '({})'.format(i)
