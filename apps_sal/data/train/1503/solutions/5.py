def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


t = int(input())
for i in range(t):
    (a, b) = input().split()
    (a, b) = (int(a), int(b))
    c = hcf(a, b)
    print(int(a * b / (c * c)))
