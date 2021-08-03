def next_smaller(n):
    s = str(n)
    i = next((i for i in range(len(s) - 1, 0, -1) if s[i - 1] > s[i]), len(s))
    j = next((j for j in range(len(s) - 1, i - 1, -1) if s[i - 1] > s[j]), -1)
    s = s[:i - 1] + s[j] + (s[i:j] + s[i - 1] + s[j + 1:])[::-1]
    return [int(s), -1][s[0] == '0' or j < 0]
