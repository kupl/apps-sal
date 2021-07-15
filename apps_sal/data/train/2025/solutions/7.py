n = int(input())
p = []
for i in range(2,n+1):
    isprime = True
    for j in p:
        if i % j == 0:
            isprime = False
            break
    if isprime:
        p.append(i)
ans = []
for i in p:
    k = 1
    while i ** k <= n:
        ans.append(str(i ** k))
        k += 1
print(len(ans))
print(' '.join(ans))

