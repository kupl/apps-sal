from collections import Counter


def find_discounted(s):
    s = list(map(int, s.split()))
    c, li = Counter(s), []
    for i in s:
        i = int(i)
        ans = i - (i * 0.25)
        if c.get(ans, 0):
            li.append(str(int(ans)))
            c[ans] -= 1
            c[i] -= 1
    return " ".join(li)
