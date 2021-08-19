for O in range(int(input())):
    l1 = input().split()
    l2 = input().split()
    s1 = set(l1)
    s2 = set(l2)
    s = set()
    s = s1.intersection(s2)
    if len(s) >= 2:
        print('similar')
    else:
        print('dissimilar')
