from numpy import array

for _ in range(int(input())):
    n, m = map(int, input().split())

    s = array([10] * n)

    for _ in range(m):
        i, j, k = map(int, input().split())

        s[i - 1:j] *= k

    print(sum(s) // n)
