try:
    for j in range(1, int(input()) + 1):
        ([a, b], c) = (list(map(int, input().split(' '))), 0)
        for i in range(1, a - b + 2):
            c += i
        print('Case', str(j).__add__(':'), c)
except:
    pass
