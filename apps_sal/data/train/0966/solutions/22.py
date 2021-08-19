for _ in range(int(input())):
    (n, u, d) = map(int, input().split())
    H = list(map(int, input().split()))
    parachute = 1
    lenH = len(H)
    for i in range(lenH):
        diff = 0
        if i == lenH - 1:
            break
        if H[i + 1] > H[i]:
            if H[i + 1] - H[i] > u:
                break
        elif H[i + 1] < H[i]:
            if H[i] - H[i + 1] > d:
                if parachute == 1:
                    parachute = 0
                    continue
                else:
                    break
    print(i + 1)
