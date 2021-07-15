def main():
    s = input()
    n = len(s)

    if s[n - 1] == '1' or s[0] == '0' or s[n - 2] == '0':
        print(-1)
        return

    for i in range(n - 1):
        if s[i] != s[n - i - 2]:
            print(-1)
            return

    conn = [[]]*(n + 1)
    children = []
    for i in range(1, n):
        if s[i - 1] == '0':
            children.append(i)
        else:
            conn[i] = children
            children = [i]
    conn[n] = [n - 1]

    for i in range(1, n + 1):
        for j in conn[i]:
            print(j, i)

def __starting_point():
    main()
__starting_point()
