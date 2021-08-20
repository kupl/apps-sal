try:
    t = int(input())
    for a in range(t):
        k = int(input())
        for i in range(k):
            if i == 0 or i == k - 1:
                print('*' * (i + 1))
            else:
                print('*' + ' ' * (i - 1) + '*')
except EOFError:
    pass
