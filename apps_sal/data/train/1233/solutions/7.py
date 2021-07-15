from sys import stdin

#stdin = open("input", "r")

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    m = 1
    for i in range(len(s)):
        k = set()
        k.add(s[i])
        for j in range(i + 1, len(s)):
            if s[j] in k:
                k.remove(s[j])
            else:
                k.add(s[j])
            if len(k) < 2:
                m = max(m, j - i + 1)
    print(m)

