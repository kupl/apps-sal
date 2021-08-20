for h in range(int(input())):
    s = input()
    l = list(s)
    s1 = set(s)
    if len(s1) == len(l):
        print('no')
    else:
        print('yes')
