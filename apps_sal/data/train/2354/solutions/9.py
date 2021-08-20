def __starting_point():
    password = input()
    n = int(input())
    lasts = set()
    firsts = set()
    attempts = set()
    for _ in range(n):
        attempt = input()
        attempts.add(attempt)
        firsts.add(attempt[0])
        lasts.add(attempt[1])
    if password in attempts or (password[0] in lasts and password[1] in firsts):
        print('YES')
    else:
        print('NO')


__starting_point()
