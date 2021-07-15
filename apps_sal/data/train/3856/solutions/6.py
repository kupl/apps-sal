a = [False, False]+[True]*500000; p = []
for (i, isprime) in enumerate(a):
    if isprime:
        p.append(i)
        for n in range(i*i, 500001, i): a[n] = False
dp = [p[i-1] for i in p if i-1<len(p)]
def solve(a,b):
    return sum(n for n in dp if a<=n<=b)
