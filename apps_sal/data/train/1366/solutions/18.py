for _ in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    max_sum = sum(A)
    s = 0
    c = 0
    for i in range(n):
        if s == 0 and A[i] == 0:
            continue
        else:
            s += A[i]
            c += 1
            if s == max_sum:
                break
    if c == 0:
        print(1)
    else:
        print(c)
