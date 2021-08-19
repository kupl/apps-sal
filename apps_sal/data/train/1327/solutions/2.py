for _ in range(int(input())):
    n, q = [int(a) for a in input().split()]
    v = list(map(int, input().split()))
    s = list(range(1, n + 1))
    index_s = [x for _, x in sorted(zip(v, s))]
    sorted_v = sorted(v)
    # print(index_s)
    # print(sorted_v)
    for i in range(q):
        x, y = [int(a) for a in input().split()]
        check1 = min(x, y)
        get_index1 = index_s.index(check1)
        vx = sorted_v[get_index1]

        check2 = max(x, y)
        get_index2 = index_s.index(max(x, y))
        vy = sorted_v[get_index2]

        length = get_index2 - get_index1 + 1
        ans = vy - vx + y - x
        print(ans, length)
