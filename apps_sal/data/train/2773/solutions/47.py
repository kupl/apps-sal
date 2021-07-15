import math
def calculate_years(principal, interest, tax, desired):
    # desired = principal*(1+(interest)*(1-tax))**n
    # desired/principal = (1+interest*(1-tax))**n
    # n = ln(d/p)/ln(1+eff Interest Rate)
    # return int(n)+1 if n>0 else 0
    effInt = interest*(1-tax)
    timeFloat = math.log(desired/principal)/math.log(1+effInt)
    if desired>principal:
        return int(timeFloat)+1
    else:
        return 0

