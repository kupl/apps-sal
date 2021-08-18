
try:
    import sys

    num = int(input())
    brackets = list(map(int, sys.stdin.readline().strip().split()))

    max_len_seq = 0
    start_max_len_seq = 0
    max_depth = 0
    start_depth = 0

    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0

    n = 0

    for i in range(num):
        if n == 0:
            t2 = i

        b = brackets[i]

        if b == 1:
            n += 1
            t3 += 1
            t4 = i
            t1 += 1

        elif b == 2:
            n -= 1
            t1 += 1
            t3 -= 1

        if t3 > max_depth:
            max_depth = t3
            start_depth = t4

        if t1 > max_len_seq:
            max_len_seq = t1
            start_max_len_seq = t2

        if n == 0:
            t1 = 0
            t2 = 0
            t3 = 0
            t4 = 0

    print(max_depth, start_depth + 1, max_len_seq, start_max_len_seq + 1)


except:
    pass
