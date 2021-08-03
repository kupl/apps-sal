n = int(input())
lis = list(map(int, input().split()))
m = 0
for a in lis:
    m = m ^ a
for a in lis:
    print(m ^ a, end=" ")
