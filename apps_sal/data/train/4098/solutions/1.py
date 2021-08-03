def new_numeral_system(n): return ['%c + %c' % (65 + i, ord(n) - i)for i in range(ord(n) - 63 >> 1)]
