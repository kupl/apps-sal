def pow(x, y):
  return x**y

# assuming python 3 where print is a function
printPow = compose(print, pow)
# compose would return
lambda *x: print(pow(*x))
# because f is bound to print and g is bound to pow.

printPow(2, 3)
# this would call the lambda with x bound to [2, 3]
# so that gives you the expression:
print(pow(*[2, 3]))
# or equivalently:
print(pow(2, 3))

