n = int(input())
A = list(map(int, input().split()))
A.sort()
b = A[0] + A[-1] + 1
a = A[-1] - 1
while b - a > 1:
    e = (b + a) // 2
    Sup = 0
    for item in A:
        Sup += e - item
    if Sup >= e:
        b = e
    else:
        a = e
print(b)
