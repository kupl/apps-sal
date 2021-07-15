from itertools import permutations,combinations

def queens(queen,size):
    X,Y, rng = ord(queen[0])-97, (int(queen[1]) or 10)-1, range(size)
    q = next(p for p in permutations(rng) if p[X]==Y and all(abs(x-y)-abs(p[x]-p[y]) for x,y in combinations(rng,2)))
    return','.join(f"{ chr(x+97) }{ (1+q[x])%10 }"for x,y in enumerate(q))
