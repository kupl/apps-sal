def solve(s):
    ans = [0]
    for char in s:
        if '0' <= char <= '9':
            ans[-1] = ans [-1] * 10 + int(char)
        elif ans[-1] > 0:
            ans.append(0)
    return max(ans)


