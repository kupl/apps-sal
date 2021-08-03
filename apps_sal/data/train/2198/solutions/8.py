n = int(input())
words = [input() for _ in range(n)]
s = set()
for w in words:
    while 'kh' in w or 'u' in w:
        if 'kh' in w:
            for i in range(len(w) - 1):
                if 'kh' == w[i:i + 2]:
                    w = w[:i] + 'h' + w[i + 2:]
        else:
            for i in range(len(w)):
                if 'u' == w[i:i + 1]:
                    w = w[:i] + 'oo' + w[i + 1:]

    s.add(w)
print(len(s))
