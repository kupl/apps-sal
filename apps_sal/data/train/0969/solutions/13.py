t = int(input())
for i in range(t):
    (n, a) = input().split()
    total = 0
    for j in range(int(n)):
        b = input()
        if 'CONTEST_WON' in b:
            (b, c) = b.split()
            if int(c) > 20:
                total = total + 300
            else:
                total = total + 300 + (20 - int(c))
        if 'TOP_CONTRIBUTOR' in b:
            total = total + 300
        if 'BUG_FOUND' in b:
            (d, e) = b.split()
            total = total + int(e)
        if 'CONTEST_HOSTED' in b:
            total = total + 50
    if a == 'INDIAN':
        print(total // 200)
    else:
        print(total // 400)
