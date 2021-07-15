def is_prime(n): return all(n%p!=0 for p in range(2,int(n**0.5)+1))
stone = []

for i in range(20):
    for j in range(12):
        p = (2**i)*(3**j) + 1
        if is_prime(p): stone.append(p)

def solve(x,y):
    return sum(1 for p in stone if p>=x and p<y)
