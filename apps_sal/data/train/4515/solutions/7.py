def diff(arr):
    z = {}
    for i in range(0, len(arr)):
        s = arr[i].split('-')
        d = abs(int(s[0]) - int(s[1]))
        z.update({arr[i]: d})
    w = {k: v for (k, v) in sorted(list(z.items()), reverse=True, key=lambda x: x[1])}
    if w == {} or max(w.values()) == 0:
        return False
    else:
        return max(w, key=w.get)
