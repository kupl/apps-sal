try:
    for _ in range(int(input())):
        (x1, y1) = list(map(float, input().split()))
        (x2, y2) = list(map(float, input().split()))
        result = (y1 * x2 + y2 * x1) / (y1 + y2)
        print(result)
except Exception:
    pass
