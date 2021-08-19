def changed(colors, types, n):
    index = -1
    for i in range(n - 1, 0, -1):
        if types[i] == types[i - 1]:
            index = i - 1
            break
    if index == -1:
        colors[n - 1] = 3
        return True
    for i in range(index + 1, n):
        if colors[i - 1] == 1:
            colors[i] = 2
        else:
            colors[i] = 1
    return False


def solve(types, n, ans):
    colors = []
    colors.append(1)
    k = 1
    for i in range(1, n):
        if types[i] != types[i - 1]:
            k += 1
            if colors[-1] == 1:
                colors.append(2)
            else:
                colors.append(1)
        else:
            colors.append(colors[-1])
    k = min(k, 2)
    if colors[n - 1] == colors[0] and types[n - 1] != types[0]:
        if changed(colors, types, n):
            k += 1
    ans.append([k])
    ans.append(colors)


def main():
    ans = []
    q = int(input())
    for i in range(q):
        n = int(input())
        types = list(map(int, input().split()))
        solve(types, n, ans)
    for i in ans:
        for j in i:
            print(j, end=' ')
        print()


main()
