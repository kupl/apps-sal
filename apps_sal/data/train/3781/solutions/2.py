def prod_int_partII(n, s):
    part = list(mul_part_gen(n))[:-1]
    sub = [p for p in part if len(p) == s]
    return [len(part), len(sub), sub[0] if len(sub) == 1 else sub]

def mul_part_gen(n, k=2): 
    if n == 1: 
        yield [] 
    for i in range(k, n+1): 
        if n % i == 0: 
            for part in mul_part_gen(n//i, i): 
                yield [i] + part

