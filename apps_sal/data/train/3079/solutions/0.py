def big_primefac_div(n):
    bpf, bd = 0, 1
    frac = []
    
    if n % 1 != 0:
        return "The number has a decimal part. No Results"
    else:
        n = abs(int(n))
        n_copy = n
  
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            frac.append(i)
        else:
            i += 1
    if n > 1: frac.append(n)

    bpf = max(frac)
    bd = n_copy / frac[0]
            
    if bpf == 0 or bd == 1:
        return []
    else:
        return [bpf, bd]
