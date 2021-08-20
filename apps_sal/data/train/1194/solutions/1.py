for _ in range(int(input())):
    n = int(input())
    s = input()
    x = 0
    y = 0
    rm = 0
    x += s.count('R') - s.count('L')
    y += s.count('U') - s.count('D')
    if y <= 0:
        rm += s.count('U') + s.count('D') + y
    else:
        rm += s.count('U') + s.count('D') - y
    if x <= 0:
        rm += s.count('L') + s.count('R') + x
    else:
        rm += s.count('L') + s.count('R') - x
    print(rm)
