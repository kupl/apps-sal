def longest_palindrome(s):
    """"Based on Manacher algorithm"""

    if s == "":
        t = "^#$"
    else:
        t = "^#" + "#".join(s) + "#$"

    c = 0
    r = 0
    p = [0] * len(t)

    for i in range(1, len(t) - 1):

        mirror = 2 * c - i
        p[i] = max(0, min(r - i, p[mirror]))

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > r:
            c = i
            r = i + p[i]

    k, i = 0, 0
    for j, e in enumerate(p):
        if e > k:
            k, i = e, j

    deb, fin = ((i - k) // 2, (i + k) // 2)
    return s[deb:fin]
