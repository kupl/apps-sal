ans = [0 for i in range(44)]
hash1 = [False for i in range(44)]


def Dfs(num, cnt):

    if(num == cnt):
        return True

    for i in range(1, cnt + 1):
        if not hash1[i] and (not((i + ans[num])**0.5 % 1)):
            ans[num + 1] = i
            hash1[i] = True
            if Dfs(num + 1, cnt):
                return True
            hash1[i] = False
    return False


def square_sums_row(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            hash1[j] = False
        ans[1] = i
        hash1[i] = True
        if Dfs(1, n):
            return ans[1: n + 1]

    return False
