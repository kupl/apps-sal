def find_missing(sequence):
    s = set(sequence)
    m1, m2 = min(s), max(s)
    for i in range(m1, m2 + 1, (m2 - m1) // len(s)):
        if i not in s:
            return i
