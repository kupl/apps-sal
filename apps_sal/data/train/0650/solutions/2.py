def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


def printMaxActivities(s, f):
    n = len(f)
    i = 0
    cnt = 1
    for j in range(n):
        if s[j] >= f[i]:
            cnt += 1
            i = j
    return cnt


for _ in range(int(input())):
    n, k = map(int, input().split())
    mat = []
    for i in range(k):
        mat.append([[], []])
    for i in range(n):
        a, b, c = map(int, input().split())
        mat[c - 1][0].append(a)
        mat[c - 1][1].append(b)
    ans = 0
    for i in range(k):
        if len(mat[i][0]) == 1:
            ans += 1
        elif len(mat[i][0]) > 1:
            ans += printMaxActivities(sort_list(mat[i][0], mat[i][1]), sorted(mat[i][1]))
    print(ans)
