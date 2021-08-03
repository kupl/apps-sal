t = float(input())
while(t):
    t -= 1
    x, k = list(map(float, input().split()))
    k = int(k)
    a = list(map(float, input().split()))
    b = list(map(float, input().split()))
    temp = x
    for i in range(0, k):
        xxx = (temp * a[i]) / b[i]
        temp += xxx
    px = (temp - x) / temp * 100.0
    print(int(px))
