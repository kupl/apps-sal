import math
def calculate_years(principal, interest, tax, desired): 
    #if principal is lower than zero, than error with return code -1
    return -1 if principal < 0 else math.ceil(math.log(float(desired) / principal if principal else 1, 1 + interest * (1 - tax)))
