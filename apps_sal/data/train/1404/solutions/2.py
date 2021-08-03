R = G = B = atmpt = counter = 0
t = int(input())
for i in range(t):
    R, G, B = list(map(int, input().split()))
    k = int(input())
    if R < k:
        atmpt = R
    else:
        atmpt = k - 1
    if G < k:
        atmpt = atmpt + G
    else:
        atmpt = atmpt + k - 1
    if B < k:
        atmpt = atmpt + B
    else:
        atmpt = atmpt + k - 1
    atmpt = atmpt + 1
    print(atmpt)
    atmpt = 0
