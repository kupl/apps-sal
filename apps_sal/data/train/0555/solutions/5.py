for _ in range(eval(input())):
    n = eval(input())
    A = list(map(int, input().split()))
    if n < 3:
        print(n)
    elif n == 3:
        print(2 if A[2] != A[0] + A[1] else 3)
    else:
        st = 1
        max_len = 0
        for i in range(2, n):
            if A[i] != A[i - 1] + A[i - 2]:
                max_len = max(max_len, i - st)
                st = i
        max_len = max(max_len, (i - st) + 1) if st < n - 1 else max_len
        print(max_len + 1)
