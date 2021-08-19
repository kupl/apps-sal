s = int(input())
while s > 0:
    s -= 1
    a = input()
    c = 0
    for x in a:
        c += int(x)
    if c < 9 and len(a) != 1:
        print(9 - c % 9)
    else:
        print(min(9 - c % 9, c % 9))
