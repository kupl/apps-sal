n = input()
n = int(n)
for i in range(0, n):
    (r, c, j, k, m) = list(map(int, input().split(' ')))
    if r * c != m + k + j:
        print('No')
    elif m % c == 0 and k * c % (j + k) == 0 and (j * c % (j + k) == 0):
        print('Yes')
    elif j % c == 0 and k * c % (m + k) == 0 and (m * c % (m + k) == 0):
        print('Yes')
    elif k % c == 0 and j * c % (j + m) == 0 and (m * c % (j + m) == 0):
        print('Yes')
    elif m % r == 0 and k * r % (j + k) == 0 and (j * r % (j + k) == 0):
        print('Yes')
    elif j % r == 0 and k * r % (m + k) == 0 and (m * r % (m + k) == 0):
        print('Yes')
    elif k % r == 0 and j * r % (m + j) == 0 and (m * r % (m + j) == 0):
        print('Yes')
    elif k % c == 0 and j % c == 0 and (m % c == 0):
        print('Yes')
    elif k % r == 0 and j % r == 0 and (m % r == 0):
        print('Yes')
    else:
        print('No')
