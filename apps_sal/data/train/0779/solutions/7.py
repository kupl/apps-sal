try:

    T = int(input())
    for i in range(T):
        n = int(input())
        path = [int(i) for i in input().strip().split(" ")]
        path.sort(reverse=True)
        count = 0
        for i in range(n - 1):
            res = (path[i] + path[i + 1]) / 2
            count = count + res
            path[i + 1] = res
        print("%.8f" % res)
except EOFError:
    pass
