from math import factorial
strong_num = lambda n: 'STRONG!!!!' if  n == sum(factorial(int(d)) for d in str(n)) else 'Not Strong !!'
