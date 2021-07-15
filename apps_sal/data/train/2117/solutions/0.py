def read_data():
    n = int(input())
    hs = list(map(int, input().split()))
    return n, hs


def solve(n, hs):
    left = get_left_index(n, hs)
    right = get_right_index(n, hs)
    vals = [[] for i in range(n)]
    for h, l, r in zip(hs, left, right):
        vals[r - l - 2].append(h)
    min_hs = []
    min_h = - float('inf')
    for val in vals[::-1]:
        for v in val:
            min_h = max(min_h, v)
        min_hs.append(min_h)
    print(* min_hs[::-1])


def get_left_index(n, hs):
    left = []
    stack = []
    for i, h in enumerate(hs):
        while stack and hs[stack[-1]] >= h:
            del stack[-1]
        if stack:
            left.append(stack[-1])
        else:
            left.append(-1)
        stack.append(i)
    return left


def get_right_index(n, hs):
    hs.reverse()
    tmp = get_left_index(n, hs)
    hs.reverse()
    tmp.reverse()
    right = [n - 1 - a for a in tmp]
    return right

n, hs = read_data()
solve(n, hs)
