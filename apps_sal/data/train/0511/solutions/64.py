n = int(input())
a = list(map(int, input().split()))

x = a[0]
for i in a[1:]:
    x ^= i

for i in a:
    print(x ^ i, end=" ")
