import math
Q = int(input())
A_list = []
B_list = []
for _ in range(Q):
    A, B = list(map(int, input().split()))
    A_list.append(min(A, B))
    B_list.append(max(A, B))

for i in range(Q):
    A = A_list[i]
    B = B_list[i]
    R = int(math.sqrt(A * B))

    if A >= B - 1:
        print((2 * A - 2))
    elif R * R == A * B:
        print((2 * R - 3))
    elif R * (R + 1) >= A * B:
        print((2 * R - 2))
    else:
        print((2 * R - 1))
