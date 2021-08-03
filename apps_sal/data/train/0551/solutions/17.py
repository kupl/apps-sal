for _ in range(int(input())):
    s = input()
    l1 = len(s)
    l2 = len(set(s))
    if l1 != l2:
        print('yes')
    else:
        print('no')
