def update(fenwick, n, ind, val):
    while ind <= n:
        fenwick[ind] += val
        ind += ind & -ind


def get(arr, ind):
    su = 0
    while ind > 0:
        su += arr[ind]
        ind -= ind & -ind
    return su


(n, m, c) = list(map(int, input().strip().split(' ')))
fenwick = [0] * (n + 1)
for z in range(m):
    s = list(map(str, input().strip().split(' ')))
    if s[0] == 'S':
        update(fenwick, n, int(s[1]), int(s[3]))
        update(fenwick, n, int(s[2]) + 1, -int(s[3]))
    else:
        print(get(fenwick, int(s[1])) + c)
