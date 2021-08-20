for _ in range(0, int(input())):
    (ans, [l, m, n]) = (['NO', 'YES'], list(map(int, input().split())))
    o = list(map(int, input().split())) + [n]
    print(ans[m % sum(o) == 0])
