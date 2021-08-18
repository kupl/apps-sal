from collections import Counter
for _ in range(int(input())):
    s = input()
    c = Counter(s)
    if c['L'] >= 2 and c['T'] >= 2 and c['I'] >= 2 and c['M'] >= 2:

        if len(s) == 9:
            if c['E'] >= 1:
                print('YES')
            else:
                print('NO')

        elif len(s) > 9:
            if c['E'] >= 2:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')
