t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = [0] * n
    max_elem = 0
    want_indices = [[], []]
    for (i, d) in enumerate(map(int, s)):
        if not want_indices[d]:
            max_elem += 1
            ans[i] = max_elem
            want_indices[1 - d].append(max_elem)
        else:
            index = want_indices[d].pop()
            ans[i] = index
            want_indices[1 - d].append(index)
    print(max_elem)
    print(*ans, sep=' ')
