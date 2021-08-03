for _ in range(int(input())):
    n = int(input())
    arr = list(range(1, n + 1))
    for i in range(n):
        print(*(arr[i:] + arr[:i]), sep='')
