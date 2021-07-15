def socialist_distribution(a, m):
    new = [i - m for i in a]
    while any(i > 0 for i in new) or sum(new)==0:   
        if all((i + m) >= m for i in new) : return [i + m for i in new]
        new[new.index(max(new))] -= 1
        new[new.index(min(new))] += 1
    return []
