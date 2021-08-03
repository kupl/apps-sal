def save(s, hd):
    return len([k for i, k in enumerate(s) if sum(s[:i + 1]) <= hd])
