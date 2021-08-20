t = eval(input())
while t:
    t -= 1
    (x, k) = list(map(int, input().split()))
    a = list(map(float, input().split()))
    b = list(map(float, input().split()))
    rat = 1.0
    for i in range(k):
        rat = rat * ((a[i] + b[i]) / b[i])
    rat = (rat - 1) / rat * 100.0
    print(int(rat))
