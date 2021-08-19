# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    mid = n // 2 - 1
    max_beg = max(l)
    f_o = l.index(max_beg)
    l.reverse()
    l_o = l.index(max_beg)
    l_o = n - 1 - l_o
    if l_o - f_o >= mid:
        print(0)
    else:
        if f_o == l_o:
            f_o = mid
            print(n - 1 - f_o)
        else:
            gap = l_o - f_o
            f_o = mid
            l_o = f_o + gap
            print(n - 1 - l_o)
