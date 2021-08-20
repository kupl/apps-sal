import math
for i in range(int(input())):
    (N, D) = list(map(int, input().split()))
    n = list(map(int, input().split()))
    days = 0
    if D == 1:
        print(len(n))
    else:
        l = [k for k in n if k >= 80 or k <= 9]
        a = math.ceil((len(n) - len(l)) / D)
        b = math.ceil(len(l) / D)
        print(a + b)
