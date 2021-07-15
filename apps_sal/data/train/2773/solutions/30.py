import math

def calculate_years(principal, interest, tax, desired):
    if principal != desired:
        return int(math.log((desired*(1+interest-interest*tax))/(principal+principal*interest*(1-tax)), 1+interest-interest*tax))+1
    else:
        return 0
