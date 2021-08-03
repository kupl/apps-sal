def pascal(p):
    ans = []
    for i in range(p):
        row = []
        for k in range(i + 1):
            if k == 0 or k == i:
                row.append(1)
            else:
                row.append(ans[i - 1][k - 1] + ans[i - 1][k])

        ans.append(row)
    return ans
