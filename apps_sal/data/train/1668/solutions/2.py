def swap(s, a, b):
    s = list(s)
    s[a], s[b] = s[b], s[a]
    return ''.join(s)


def maximized_range(s, left):
    return s[:left] + ''.join(sorted(s[left:], reverse=True))


def next_smaller(n):
    s = str(n)
    k = len(s)
    for i in range(k - 1, -1, -1):
        for j in range(k - 1, i, -1):
            if s[j] < s[i]:
                t = swap(s, i, j)
                if t[0] != '0':
                    return int(maximized_range(t, i + 1))
    return -1
