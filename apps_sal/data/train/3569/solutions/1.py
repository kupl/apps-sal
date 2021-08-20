def is_lucky(t):
    return len(t) == 6 and t.isdigit() and (sum(map(int, t[:3])) == sum(map(int, t[3:])))
