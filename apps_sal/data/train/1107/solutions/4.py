
t = int(input())

for i in range(t):

    l, r = map(int, input().split())
    start = len(str(l))
    end = len(str(r))
    if end > start:
        end_start = int(str('9' * start))
        sum_start = ((end_start + l) * start * ((end_start - l + 1))) // 2
    else:
        sum_start = ((l + r) * start * (r - l + 1)) // 2

    sum = 0

    for j in range(start + 1, end):
        sum += ((10**(j - 1) + (int(str('9' * j)))) * j * (((int(str('9' * j)) - (10**(j - 1)) + 1)))) // 2

    if end > start:
        end = len(str(r))
        end__start = int(str(10**(end - 1)))
        sum__start = ((end__start + r) * end * (r - end__start + 1)) // 2
    else:
        sum__start = 0
    print((sum + sum__start + sum_start) % 1000000007)
