def solve(s, l, ans):
    n = len(s)
    s = list(s)
    if l > 1:
        s.sort()
        ans.append(s)
        return

    indices = []
    min_val = min(s)
    for i in range(len(s)):
        if s[i] == min_val:
            indices.append((i, 1))

    while True:
        min_val = 'z'
        found = False
        for index, count in indices:
            min_val = min(min_val, s[index])
            if count == n:
                found = True

        if found:
            break

        new_indices = []
        for index, count in indices:
            if s[index] == min_val:
                if index + 1 == n:
                    new_indices.append((0, count + 1))
                else:
                    new_indices.append((index + 1, count + 1))

        indices = new_indices[:]

    s1 = []
    index = indices[0][0]
    count = 0
    while index >= 0:
        s1.append(s[index])
        count += 1
        index -= 1

    index = n - 1
    while count != n:
        s1.append(s[index])
        index -= 1
        count += 1

    s1.reverse()
    ans.append(s1)


def main():
    t = int(input())
    ans = []
    for i in range(t):
        l, s = map(str, input().split())
        l = int(l)
        solve(s, l, ans)

    for i in ans:
        for j in i:
            print(j, end='')

        print()


main()
