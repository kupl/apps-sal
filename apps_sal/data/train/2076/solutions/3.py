d = lambda i, j, k: sum((a - c) * (b - c) for a, b, c in zip(p[i], p[j], p[k])) * (i != j)

n = int(input())

r = list(range(n))

p = [list(map(int, input().split())) for i in r]

t = [k + 1 for k in r if all(d(i, j, k) <= 0 for i in r for j in r)] if n < 12 else []

for q in [len(t)] + t: print(q)



# Made By Mostafa_Khaled

