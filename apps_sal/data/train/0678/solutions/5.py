# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    an = 0
    ix = 0
    cr = l[0]
    pr = [l[0]]
    for i in range(1, n):
        pr.append(pr[-1] + (l[i]))
    # print(pr)
    while ix < n - 1:
        an += 1
        ix += cr
        if ix < n - 1:
            cr = pr[ix]
    print(an)
