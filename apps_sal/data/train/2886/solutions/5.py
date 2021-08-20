def find(s):
    if s == '' or '!' not in s or '?' not in s:
        return ''
    s += ' '
    counts = []
    curr = s[0]
    count = 0
    for i in s:
        if i == curr:
            count += 1
        else:
            counts.append(count)
            count = 1
            curr = i
    n = []
    for i in range(len(counts) - 1):
        n.append(counts[i] + counts[i + 1])
    x = n.index(max(n))
    a = sum(counts[:x])
    return s[a:a + counts[x] + counts[x + 1]]
