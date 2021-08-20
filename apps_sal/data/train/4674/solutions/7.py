def rank(st, we, n):
    if not st:
        return 'No participants'
    names = st.split(',')
    if len(names) < n:
        return 'Not enough participants'
    result = {names[i]: (sum((ord(l.lower()) - ord('a') + 1 for l in names[i])) + len(names[i])) * we[i] for i in range(len(names))}
    result = {k: v for (k, v) in sorted(result.items(), key=lambda item: item[0])}
    result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    return result[n - 1][0]
