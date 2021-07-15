def rank(st, we, n):
    if not st: return "No participants"
    st = st.split(',')
    calc = lambda x: we[x[0]] * (len(x[1]) + sum(ord(m) - ord('a') + 1 for m in x[1].lower()))
    return sorted(sorted([m for m in enumerate(st)], key=lambda x: x[1]), key=lambda m: calc(m), reverse=True)[n - 1][1] if len(st) >= n else "Not enough participants"
