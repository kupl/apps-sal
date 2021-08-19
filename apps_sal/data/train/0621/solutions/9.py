def sub(s1, s2):
    m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
    (longest, x_longest) = (0, 0)
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest:x_longest]


test = eval(input())
while test:
    test -= 1
    n = eval(input())
    arr1 = list(map(str, input().split()))
    arr = []
    for i in range(n):
        ans = arr1[i]
        for j in range(n):
            ans = sub(ans, arr1[j])
        arr.append(ans)
    oth_arr = []
    length = 0
    for i in range(len(arr)):
        length = max(length, len(arr[i]))
    for i in range(len(arr)):
        if len(arr[i]) == length:
            oth_arr.append(arr[i])
    oth_arr.sort()
    print(oth_arr[0])
