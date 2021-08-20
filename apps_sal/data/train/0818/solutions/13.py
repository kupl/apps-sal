x = int(input())
for y in range(x):
    N = int(input())
    Z = list(map(int, input().split()))
    P = int(input())
    Z1 = [0]
    count = 0
    for q in range(N):
        if Z[q] % 2 == 0:
            count += 1
        Z1.append(count)
    for t in range(P):
        (i, j) = list(map(int, input().split()))
        if Z1[j] - Z1[i - 1] > 0:
            print('EVEN')
        else:
            print('ODD')
