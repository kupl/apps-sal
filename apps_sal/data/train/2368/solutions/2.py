for _ in range(int(input())):
    am = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    aMin = min(a)
    bMin = min(b)
    t = 0
    for i in range(am):
        t += max(a[i] - aMin, b[i] - bMin)
    print(t)
