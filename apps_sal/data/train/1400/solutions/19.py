def get_sum(k):
    if k == 1:
        return 1

    return 2**(k - 1) + get_sum(k - 1)


t = int(input())

for _ in range(t):

    n, l, r = map(int, input().split())

    minimum = (n - l) + get_sum(l)
    maximum = get_sum(r) + (n - r) * int(2**(r - 1))

    print('{} {}'.format(minimum, maximum))
