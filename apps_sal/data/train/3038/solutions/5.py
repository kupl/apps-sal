def solve(st):
    dict = {'z': 0}
    for letter in set(st) : 
        this = [a for a in range(len(st)) if st[a] == letter]
        that = max(this) - min(this)
        if that > max(dict.values()) : dict = {letter : that}
        elif that == max(dict.values()) : dict[letter] = that
    return sorted(dict.keys(),reverse=False)[0]
