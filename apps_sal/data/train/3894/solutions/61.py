def solve(s):
    num_upper = sum([1 for ch in s if ch.isupper()])
    num_lower = sum([1 for ch in s if ch.islower()])
    if num_upper > num_lower:
        return s.upper()
    return s.lower()
