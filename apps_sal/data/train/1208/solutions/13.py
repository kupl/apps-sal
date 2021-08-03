t = int(input())
n = []
for i in range(t):
    num = int(input())
    n.append(num)
fact = [1]
facti = [1]
for i in range(1, max(n) + 1):
    fact.append(i * fact[i - 1] % 1000000007)
    facti.append(facti[i - 1] * fact[i] % 1000000007)
for i in n:
    print(facti[i])
