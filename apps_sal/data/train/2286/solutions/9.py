import sys
input = sys.stdin.readline

K, N = map(int, input().split())

if K % 2 == 0:
    L = K // 2
    R = L + 1
    arr = [L] + [K] * (N - 1)
else:
    """
    [3,3,3,3,3] だと 手前に3 33 333 3333 が余分。2歩戻る。
    """
    arr = [(K + 1) // 2] * N
    x = N // 2
    for i in range(x):
        arr[-1] -= 1
        if arr[-1] == 0:
            arr.pop()
            continue
        L = len(arr)
        if L < N:
            arr += [K] * (N - L)

answer = ' '.join(map(str, arr))
print(answer)
