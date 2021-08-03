ddd = 0


def prime(n):
    if n < 2:
        return []
    else:
        n += 1
        save = [True] * (n // 2)
        for i in range(3, int(n ** 0.5) + 1, 2):

            if save[i // 2]:
                k = i * i
                save[k // 2::i] = [False] * ((n - k - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if save[i]]


pp = prime(1000000)


def decom(x):
    nns = 0
    arrr = 0
    answer = 1
    while (x != 1):
        nonlocal ddd
        ddd += 1
        while (x % pp[nns] == 0):
            x = x / pp[nns]
            arrr += 1
        if arrr != 0:
            answer = answer * (arrr + 1)
            arrr = 0
        nns += 1
    return answer - 2


rr = int(input())
p = 0
for i in range(rr):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    ss = arr[0] * arr[n - 1]
    f = 0
    for i in range(n):
        ddd += 1
        if arr[i] * arr[n - 1 - i] != ss:
            f = 1
            break
    if decom(ss) != n:
        f = 1
    if f == 1:
        print(-1)
    else:
        print(ss)
