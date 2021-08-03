def binary_simulation(s, q):
    s = '0' + s
    ans = []
    for val in q:
        if val[0] == 'I':
            s = s[:val[1]] + s[val[1]: val[2] + 1].translate(''.maketrans('01', '10')) + s[val[2] + 1:]
        elif val[0] == 'Q':
            ans.append(s[val[1]])
    return ans
