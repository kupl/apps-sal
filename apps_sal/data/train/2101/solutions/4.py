I = input
Vertix, edge = list(map(int,I().split()))
edges = set(tuple(map(int, I().split())) for _ in range(edge))
Universal_set = set(range(1, Vertix+1))
queu = []
cost = 0
while Universal_set:
    if queu:
        pop = queu.pop()
    else:
        pop = Universal_set.pop()
        cost += 1
    next = {v for v in Universal_set if (pop, v) not in edges and (v, pop) not in edges}
    Universal_set -= next
    queu += next

print(cost - 1)

