t = int(input())
for i in range(0, t):
    (n, m) = map(int, input().split())
    arr = []
    ans = []
    for i in range(0, n):
        in_arr = list(map(int, input().split()))
        if i == 0:
            x = '1' * m
        else:
            x = ''
            for j in range(0, m):
                arr2 = [0] * m
                if j == 0:
                    maxv = max(ans[i - 1][0], ans[i - 1][1])
                elif j == m - 1:
                    maxv = max(ans[i - 1][m - 2], ans[i - 1][m - 1])
                else:
                    maxv = max(ans[i - 1][j - 1], ans[i - 1][j], ans[i - 1][j + 1])
                if maxv > in_arr[j]:
                    in_arr[j] = maxv
                    x = x + '0'
                else:
                    x = x + '1'
        ans.append(in_arr)
        arr.append(x)
    for i in range(0, n):
        print(arr[i])
