def divisor_sum(n):
    s = 0; i = 1
    while i*i<=n:
        if n%i==0: s+=i+n//i
        i+=1
    if (i-1)**2 == n: s -= (i-1)
    return s

ratios = {}
for i in range(2,7001):
    d = divisor_sum(i); ratio = d/i
    if ratio in ratios: ratios[ratio] += [i]
    else: ratios[ratio] = [i]
ratios = [v for k, v in ratios.items() if len(v)>1]

def solve(a,b):
    d = [[r for r in v if r>=a and r<b] for v in ratios]
    return sum(min(v) for v in d if len(v)>1)
