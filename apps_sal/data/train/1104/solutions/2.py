mod = 10**9 + 7
for t in range(int(input())):
    n, k = map(int, input().split())
    if n == 0:
        if k == 1:
            print(0)
        else:
            print(int((k * (1 + k)) / 2) % mod)
        continue
    futile_moves = (n - 1)
    if k == 1:
        f_time = futile_moves * (1 + futile_moves)
        print((f_time + n) % mod)
        continue
    k -= 1
    futile_moves += 1
    if k % 2 == 0:
        futile_moves += (int(k / 2) - 1)
    else:
        futile_moves += int(k / 2)
    f_time = futile_moves * (1 + futile_moves)
    if k % 2 == 0:
        f_time += (futile_moves + 1) * 2 - n
    else:
        f_time += n
    f_time %= mod
    print(f_time)
