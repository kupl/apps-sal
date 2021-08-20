def gcd(a, b):
    while b > 0:
        (a, b) = (b, a % b)
    return a


a = [4, 10, 16, 14]
(n, r) = map(int, input().split())
lst = [r]
lst.extend(list(map(int, input().split())))
nlst = []
for i in range(0, n - 1):
    nlst.append(lst[i + 1] - lst[i])
result = nlst[0]
for i in nlst[1:]:
    result = gcd(result, i)
print(result)
