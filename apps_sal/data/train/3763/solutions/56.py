def calculator(x, y, op):
    try:
        return float({'+': int.__add__, '-': int.__sub__, 
                      '*': int.__mul__, '/': int.__truediv__}[op](x, y))
    except:
        return 'unknown value'
