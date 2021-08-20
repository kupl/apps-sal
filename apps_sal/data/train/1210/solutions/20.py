t = int(input())
for i in range(t):
    (a, b) = list(map(int, input().split()))
    (c, d) = input().split()
    if c == 'L':
        sonu = b
        if d == 'H':
            if sonu % 2 != 0:
                print(str(sonu), 'H')
            else:
                print(str(sonu), 'E')
        elif sonu % 2 != 0:
            print(str(sonu), 'E')
        else:
            print(str(sonu), 'H')
    else:
        sonu = a - b + 1
        if d == 'H':
            if sonu % 2 != 0:
                print(str(sonu), 'H')
            else:
                print(str(sonu), 'E')
        elif sonu % 2 != 0:
            print(str(sonu), 'E')
        else:
            print(str(sonu), 'H')
