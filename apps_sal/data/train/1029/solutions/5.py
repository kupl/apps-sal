def solve():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        cmpl = [int(x) for x in input().split()]
        uncmpl = [i for i in range(1, n + 1) if i not in cmpl]
        l1 = []
        l2 = []
        for i in range(len(uncmpl)):
            if i & 1 == 0:
                l1.append(uncmpl[i])
            else:
                l2.append(uncmpl[i])
        print(*l1)
        print(*l2)


# import sys
# def fast():
#     sys.stdin = open("input.txt", "r")
#     sys.stdout = open("output.txt", "w")
# fast()
solve()
