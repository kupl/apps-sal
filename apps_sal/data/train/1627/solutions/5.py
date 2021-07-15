CHARS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def base(number, base):
    return sum([num * base**coeff for coeff, num in enumerate(number[::-1])])

def bias_checker(n, b, slicer=0):
    if n[0] == b:
        n[0]=0
        n.insert(0,1)
    elif n[-1+ slicer] == b:
        n[-1 + slicer] = 0
        n[-2 + slicer] += 1
        bias_checker(n, b, slicer-1)
    return

def get_polydivisible(n, b):
    num = [0]
    count = 0
    polydiv_num = 0
    while count < n:
        for x in range(1, len(num)+1):
            if base(num[:x], b) % x != 0:
                num[-1] += 1
                bias_checker(num, b)                
                break
        else:
            count += 1
            polydiv_num = num
            num[-1] += 1
            bias_checker(num, b)
    num[-1] -= 1
    return "".join([CHARS[x] for x in num]) 

def is_polydivisible(s, b):
    num = [CHARS.find(x) for x in s]
    for x in range(1,len(num)+1):
        if base(num[:x],b) % x != 0:
            return False
    return True
