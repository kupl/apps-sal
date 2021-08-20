for _ in range(int(input())):
    (N, A, B, K) = map(int, input().split())
    cnt = 0
    for i in range(1, N + 1):
        (a, b) = (i % A, i % B)
        if a == 0 and b != 0:
            cnt += 1
        elif a != 0 and b == 0:
            cnt += 1
        if cnt >= K:
            print('Win')
            break
    else:
        print('Lose')
