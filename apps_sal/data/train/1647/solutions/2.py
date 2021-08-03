def next_bigger(n):
    n = str(n)[::-1]
    try:
        i = min(i + 1 for i in range(len(n[:-1])) if n[i] > n[i + 1])
        j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
        return int(n[i + 1::][::-1] + n[j] + ''.join(sorted(n[j + 1:i + 1] + n[:j])))
    except:
        return -1
