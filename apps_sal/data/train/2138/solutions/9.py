n = input().count('1')
m = input().count('1')
print('YNEOS'[n + (n & 1) < m::2])

