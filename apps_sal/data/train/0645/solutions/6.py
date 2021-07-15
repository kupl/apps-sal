t = int(input())
for test in range(t):
 n = int(input())
 k = int(input())
 one = k % n
 zero = n - one
 if zero < one:
  one, zero = zero, one

 if zero >= one + 1:
  print(one * 2)
 elif zero == one:
  print(2 * zero - 1)
 else:
  print((zero - 1) * 2)


