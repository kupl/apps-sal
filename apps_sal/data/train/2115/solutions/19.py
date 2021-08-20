(a, b) = input().split()
n = int(a)
d = int(b)
_point = [int(i) for i in input().split()]
k = 0
S = 0
for i in range(2, n):
    while _point[i] - _point[k] > d:
        k += 1
    Nu = i - k
    S += Nu * (Nu - 1) // 2
print(S)
