def solve(n, k):
    s = str(n)
    Slen = len(s)
    removed = False
    largestIndex = 0
    if (Slen < 2 and k > 1) or k > Slen:
        return '0'
    i = 1
    for j in range(k):
        while i < len(s):
            if s[i] < s[i - 1]:
                s = s[:i - 1] + s[i:]
                removed = True
                break
            i += 1
        i = 1
        if not removed:
            largestIndex = 0
            j = 0
            while not removed and j < len(s):
                if int(s[j]) > int(s[largestIndex]):
                    largestIndex = j
                j += 1
            s = s[:j - 1] + s[j:]
        removed = False
    return s
