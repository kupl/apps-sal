fac = 1
facts = [1]
for i in range(1, 100000):
    fac = (fac * (2 * i + 1) * (i + 1)) % 1000000007
    facts.append(fac)

T = int(input())

for _ in range(T):
    N = int(input())
    print(facts[N - 1])
