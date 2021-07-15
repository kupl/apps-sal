from collections import defaultdict

D = defaultdict(list)
for x in range(1, 2000):
    D[sum(y for y in range(1, x+1) if x%y == 0) / x].append(x)
result = [v for v in D.values() if len(v) >= 2]

# Fuck [6, 28, 496] and [84, 270, 1488, 1638], description was unclear
def solve(a,b):
    def check(p):
        for x in range(len(p)-1):
            if a <= p[x] and p[x+1] < b:
                return p[x]
        return 0
    return sum(map(check, result))
