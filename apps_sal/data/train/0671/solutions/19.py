for _ in range(int(input())):
    (n, s) = map(int, input().split())
    arr_price = list(map(int, input().split()))
    arr_players = list(map(int, input().split()))
    a = b = 101
    for i in range(n):
        if arr_players[i] == 0:
            a = min(a, arr_price[i])
            if s + a + b <= 100:
                print('yes')
                break
        else:
            b = min(b, arr_price[i])
            if s + a + b <= 100:
                print('yes')
                break
    else:
        print('no')
