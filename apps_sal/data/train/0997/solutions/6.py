for test_case in range(int(input())):
    (n, m) = list(map(int, input().split()))
    arr = [10] * n
    for i in range(m):
        (i, j, k) = list(map(int, input().split()))
        for a1 in range(i - 1, j):
            arr[a1] *= k
    print(sum(arr) // n)
