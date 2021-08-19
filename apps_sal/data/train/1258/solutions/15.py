for i in range(int(input())):
    s = input()
    rem = int(s) % 9
    n = sum(map(int, s))
    if n < 5 and len(s) > 1:
        print(9 - n)
    else:
        if rem >= 5:
            rem = 9 - rem
        print(rem)
