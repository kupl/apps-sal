def solve(s):
    sr = s[::-1]
    sr = sr.replace(' ', '')
    x = [pos for pos, char in enumerate(s) if char == ' ']
    for i in range(0, len(x)):
        sr = sr[:x[i]] + ' ' + sr[x[i]:]
    return sr
