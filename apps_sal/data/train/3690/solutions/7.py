def solve(st, idx):
    if st[idx] != "(":
        return -1
    stack = []
    for i in range(len(st)):
        if st[i] == "(":
            stack.append(i)
        elif st[i] == ")":
            tmp = stack.pop()
            if tmp == idx:
                return i
    return -1
