def win_num(name, weight):
    return (len(name) + sum((ord(c) - 96 for c in name.lower()))) * weight


def rank(st, we, n):
    if not st:
        return 'No participants'
    elif n > len(we):
        return 'Not enough participants'
    else:
        return sorted(((-win_num(s, w), s) for (s, w) in zip(st.split(','), we)))[n - 1][1]
