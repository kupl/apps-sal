for _ in range(int(input())):
    (N, U, D) = list(map(int, input().split()))
    H = list(map(int, input().split()))
    jumps = 0
    paracount = 0
    for i in range(len(H) - 1):
        if H[i + 1] - H[i] <= U and H[i + 1] >= H[i]:
            jumps += 1
        elif H[i] >= H[i + 1] and H[i] - H[i + 1] <= D:
            jumps += 1
        elif H[i] - H[i + 1] > D and paracount == 0:
            jumps += 1
            paracount = 1
        else:
            break
    print(jumps + 1)
