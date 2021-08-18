def solve(l, r, c, row, col, po):
    count = 0
    visited = set()
    stack = set()
    stack.add((l[row][col], row, col))
    while stack:
        ele = stack.pop()
        visited.add((ele[1], ele[2]))
        if ele[0] < po:
            count += 1
            if ele[1] - 1 >= 0 and (ele[1] - 1, ele[2]) not in visited:
                if l[ele[1] - 1][ele[2]] < po:
                    stack.add((l[ele[1] - 1][ele[2]], ele[1] - 1, ele[2]))
            if ele[1] + 1 < r and (ele[1] + 1, ele[2]) not in visited:
                if l[ele[1] + 1][ele[2]] < po:
                    stack.add((l[ele[1] + 1][ele[2]], ele[1] + 1, ele[2]))
            if ele[2] - 1 >= 0 and (ele[1], ele[2] - 1) not in visited:
                if l[ele[1]][ele[2] - 1] < po:
                    stack.add((l[ele[1]][ele[2] - 1], ele[1], ele[2] - 1))
            if ele[2] + 1 < c and (ele[1], ele[2] + 1) not in visited:
                if l[ele[1]][ele[2] + 1] < po:
                    stack.add((l[ele[1]][ele[2] + 1], ele[1], ele[2] + 1))
    return count


for _ in range(int(input())):
    r, c, q = map(int, input().split())
    l = []
    for i in range(r):
        a = list(map(int, input().split()))
        l.append(a)
    for i in range(q):
        row, col, po = map(int, input().split())
        print(solve(l, r, c, row - 1, col - 1, po))
