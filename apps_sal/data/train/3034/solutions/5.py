def bowling_score(s):
    (i, count) = (0, [])
    while len(count) < 9:
        count.append(s[i] + s[i + 1] + [0, s[i + 2]][10 in [s[i] + s[i + 1], s[i]]])
        i += 2 - int(s[i] == 10)
    return sum(count) + sum(s[i:])
