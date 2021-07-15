from math import factorial
from functools import reduce
import operator
def increasing_numbers(digits):
    if digits == 0:
        return 1
    if digits == 1:
        return 10
    consec_pro = reduce(operator.mul, (i for i in range(10, 10 + digits)))
    return consec_pro / factorial(digits)    
