for _ in range(int(input())):
    (dollar, cents, C) = map(int, input().split())
    mx = 100 * dollar + cents
    mx_i = 0
    for i in range(1, 10001):
        if cents >= C:
            (dollar, cents) = (cents - C, dollar)
            if 100 * dollar + cents > mx:
                mx = 100 * dollar + cents
                mx_i = i
        else:
            dollar -= 1
            cents += 100
            (dollar, cents) = (cents - C, dollar)
            if 100 * dollar + cents > mx:
                mx = 100 * dollar + cents
                mx_i = i
        if 100 * dollar + cents < C:
            break
    print(mx_i)
