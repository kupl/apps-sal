T = int(input())
for i in range(T):
    (A, B, C) = map(int, input().split())
    l = [A, B, C]
    l.sort()
    print(l[1])
