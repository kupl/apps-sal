def polydivisible(n):
    len_n = len(str(n))
    for i in range(1, len_n+1):
        if n // (10 ** (len_n - i)) % i != 0:
            return i 
    else:
        return True
            
def next_num(n): 
    n += 1
    while n <= 3608528850368400786036725: 
        pr = polydivisible(n)
        if pr == True:
            return n
        else:
            len_n = len(str(n))
            num = 10 ** (len_n - pr)
            n = (n // num + 1) * num


