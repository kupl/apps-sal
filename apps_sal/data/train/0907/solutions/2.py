for _ in range(int(input())):
    l = input()
    s = list(input())
    s = list([x for x in s if x != '.'])
    if 'T' in s[::2] or 'H' in s[1::2] or len(s) % 2 != 0:
        print('Invalid')
    else:
        print('Valid')
