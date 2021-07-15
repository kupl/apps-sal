t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]
    if max(a) != max(b):
        print("YES")
    else:
        print("NO")
