def search_substr(f_t, s_t, allow_overlap=True):
    if not s_t or not f_t:
        return 0
    if allow_overlap:
        return sum(1 for i in range(len(f_t) - len(s_t) + 1) if f_t[i: i + len(s_t)] == s_t)
    return f_t.count(s_t)
