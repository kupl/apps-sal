t = int(input())
while t > 0:
    n, m = map(int, input().split())
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))
    set_m = set(list_m)
    set_n = set(list_n)
    set_mn = set_m - set_n
    set_nm = set_n - set_m
    union_set = set_mn.union(set_nm)
    print(*sorted(list(union_set)))
    t -= 1
