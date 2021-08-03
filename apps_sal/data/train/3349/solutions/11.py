def find_missing_number(s):
    if not s:
        return 0
    elif s.replace(' ', '').isdigit():
        try:
            return [p[0] + 1 == p[1] for p in enumerate(sorted(map(int, s.split())))].index(False) + 1
        except ValueError:
            return 0
    else:
        return 1
