for _ in range(int(input())):
    n = set(input().split())
    m = set(input().split())

    if len(n.intersection(m)) >= 2:
        print('similar')
    else:
        print('dissimilar')
