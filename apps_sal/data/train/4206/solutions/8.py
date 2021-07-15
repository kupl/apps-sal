ready = [0,0,0,1]

def f(x):
    if x<len(ready): return ready[x]
    else: return f(x//2) + f(x//2 + x%2)

for i in range(4,100001):
    ready.append(f(i))


def three_details(n):
    if n < 100000: return ready[n]
    else: return three_details(n//2) + three_details(n//2 +n%2)
