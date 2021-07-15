import random
def squares(n):
    return [(i*i) for i in range(1, n+1)]

def num_range(n, start, step):
    list = []
    x = 0
    for i in range(n):
        list.append(start+x)
        x += step
    return list

def rand_range(n, mn, mx):
    return [(random.randint(mn, mx)) for i in range(n)]
    
def primes(n):
    list = []
    count = 1
    s = 2
    while count <= n-1:
        s += 1
        for i in range(2, s):
            if s%i == 0:
                break
        else:
            if i == 2:
                list.append(i)
            i += 1
            list.append(i)
            count += 1
    return list

