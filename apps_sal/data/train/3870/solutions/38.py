def solve(s):
    sl = [i for i, e in enumerate(s) if e == ' ']

    ans = list(''.join(s[::-1].split(' ')))
    for i in sl:
        # ans = list(''.join(s[::-1].split(' '))).insert(i, ' ') # Not good!!!
        ans.insert(i, ' ')
    return ''.join(ans)
