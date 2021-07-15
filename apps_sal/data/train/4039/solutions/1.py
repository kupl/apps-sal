def change_base(n, b):
    result = ''
    while n > 0:
        rem = n % b if n % b <=9 else 'x'
        result = str(rem) + result
        n //= b
    return result

def fouriest(n):
    bb, br = None, 0
    for i in range(2, n):
        res = list(change_base(n, i))
        nf = res.count('4')        
        if br >= len(res):
            break
        elif nf > br:
            br, bb = nf, i
            
    return f"{n} is the fouriest ({change_base(n, bb)}) in base {bb}"
