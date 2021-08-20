for _ in range(eval(input())):
    n = eval(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    (max, rat, ind) = (l[0] * r[0], r[0], 1)
    for i in range(1, n):
        if l[i] * r[i] >= max:
            if rat < r[i]:
                max = l[i] * r[i]
                ind = i + 1
                rat = r[i]
    print(ind)
