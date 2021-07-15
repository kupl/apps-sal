def rank(st: str, we: list, n: int):
    if not st:
        return 'No participants'
    elif n > len(st.split(',')):
        return "Not enough participants"
    
    def to_number(word):
        return (sum(ord(c.lower())-96 for c in word) + len(word))
    
    d = {}
    for w, wt in zip(st.split(','), we):
        d[w] = to_number(w) * wt
    
    sorted_d = sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))
    print(sorted_d)
    return sorted_d[n-1][0]
