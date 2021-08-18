t = int(input())
for test in range(t):
    n = int(input())
    a_set = set()
    b_set = set()
    for i in range(n):
        x, y = list(map(int, input().split()))
        a_set.add(x - y)
        b_set.add(x + y)
    a_set = list(a_set)
    b_set = list(b_set)
    if len(a_set) != n or len(b_set) != n:
        print(0)
    else:
        a_set = sorted((a_set))
        b_set = sorted((b_set))
        a1 = a_set[1] - a_set[0]
        b1 = b_set[1] - b_set[0]
        for i in range(2, n):
            a1 = min(a1, a_set[i] - a_set[i - 1])
            b1 = min(b1, b_set[i] - b_set[i - 1])
        print(min(a1, b1) / 2)
