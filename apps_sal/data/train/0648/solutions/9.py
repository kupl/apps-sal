(N, Q) = list(map(int, input().split(' ')))
ar = list(map(int, input().split(' ')))


def find_next(i, k):
    count = 0
    last = i
    ind = i + 1
    while ind < N and count < k:
        if ar[ind] > ar[last] and ind - last <= 100:
            count += 1
            last = ind
        elif ind - last > 100:
            return last
        ind += 1
    if count < k:
        return last
    return ind - 1


def change_height(L, R, K):
    for i in range(L, R + 1):
        ar[i] += K


for _ in range(Q):
    inp = list(map(int, input().split(' ')))
    if inp[0] == 1:
        (i, k) = (inp[1], inp[2])
        print(find_next(i - 1, k) + 1)
    elif inp[0] == 2:
        (L, R, K) = (inp[1], inp[2], inp[3])
        change_height(L - 1, R - 1, K)
