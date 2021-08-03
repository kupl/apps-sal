import sys
n = int(input())
col = [1 for i in range(n + 2)]
curprime = 1
ans = 0
if n <= 2:
    print(1)
    for i in range(n):
        print(1, end=' ')
    return
while True:
    prime = curprime + 1
    while prime <= n + 1 and col[prime] == 2:
        prime += 1
    if prime >= n + 1:
        break
    for i in range(prime + prime, n + 2, prime):
        col[i] = 2
    curprime = prime
print(2)
for i in range(2, n + 2):
    print(col[i], end=' ')
