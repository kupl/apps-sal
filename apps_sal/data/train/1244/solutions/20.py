n = int(input())
modulus = 10**9 + 7
s = 0
for i in range(n):
    l = list(map(int, input().split()))
    k = l[1] + 1 - l[0]
    if(l[0] < 0 and l[1] < 0):
        k = l[0] - l[1] - 1
    s += abs(k)
print(s % modulus)
