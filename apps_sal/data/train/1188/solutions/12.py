n = eval(input())
dons = input().split()
dons = [int(x) for x in dons]
dons = set(dons)
criminals = set(range(1, n + 1))
killers = criminals - dons
print(" ".join(str(x) for x in killers))
