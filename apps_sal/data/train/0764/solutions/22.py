t = int(input())
for ts in range(t):
    n = set(input().split())
    m = set(input().split())
    if len(n.intersection(m)) >= 2:
        print('similar')
    else:
        print('dissimilar')
