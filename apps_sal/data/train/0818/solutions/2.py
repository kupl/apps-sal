for _ in range(int(input())):

    t = int(input())
    arr = list(map(int, input().split()))
    prearr = [0]
    cnt = 0

    for i in range(t):
        if arr[i] % 2 == 0:
            cnt += 1

        prearr.append(cnt)

    for _ in range(int(input())):
        l, r = map(int, input().split())

        tot = prearr[r] - prearr[l - 1]
        print("EVEN") if tot > 0 else print("ODD")
