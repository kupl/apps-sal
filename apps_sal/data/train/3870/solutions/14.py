def solve(s):
    ans = list(s.replace(' ', '')[::-1])
    for i in [i for (i, item) in enumerate(s) if item == ' ']:
        ans.insert(i, ' ')
    return ''.join(ans)
