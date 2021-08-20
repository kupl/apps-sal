t = int(input())
for i in range(t):
    (n, w1, w2, w3) = map(int, input().split())
    if n >= w1 + w2 + w3:
        print(1)
    elif n >= w1 + w2 or n >= w2 + w3:
        print(2)
    else:
        print(3)
