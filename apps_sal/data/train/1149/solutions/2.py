# cook your dish here

t = 0
try:
    t = int(input())
except:
    pass


for _ in range(t):
    l = input()

    n = len(l)
    prod = 1
    for k in range(n // 2):
        i = l[k]
        j = l[n - k - 1]
        if ((i != j) and (i != '?' and j != "?")):
            prod *= 0
            break
        elif ((i == j) and (i == '?')):
            prod *= 26
        prod = prod % 10000009
    if n % 2 != 0:
        if l[n // 2] == "?":
            prod *= 26

    print(prod)
