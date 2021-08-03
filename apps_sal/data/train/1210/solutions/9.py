for i in range(int(input())):
    n, x = map(int, input().split())
    pos, lang = input().split()
    if 'L' in pos:
        x = x
    elif 'R' in pos:
        x = n - x + 1
    if x % 2 == 0 and lang == 'H':
        print(f'{x} E')
    elif x % 2 == 0 and lang == 'E':
        print(f'{x} H')
    elif x % 2 != 0:
        print(f'{x} {lang}')
