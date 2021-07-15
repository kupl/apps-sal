def super_size(n):
    result = ""
    num = sorted([int(d) for d in  str(n)])[::-1]
    for n in num:
        result += str(n) 
    return int(result)
