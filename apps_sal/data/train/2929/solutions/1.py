def factors(n):
    sq = [i for i in range(2, int(n**0.5) + 2) if n%(i*i)==0]
    cb = [i for i in range(2, int(n**(1/3) + 2)) if n%(i*i*i)==0]
    return [sq, cb]
