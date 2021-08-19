def main():
    (N, T) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if N == 1:
        return 0
    min_v = A[0]
    max_d = float('-inf')
    for i in range(1, N):
        if A[i] - min_v > max_d:
            max_d = A[i] - min_v
        if A[i] < min_v:
            min_v = A[i]
    d = set()
    d.add(A[0])
    ans = 0
    for i in range(1, N):
        if A[i] - max_d in d:
            ans += 1
        d.add(A[i])
    return ans


def __starting_point():
    print(main())


__starting_point()
