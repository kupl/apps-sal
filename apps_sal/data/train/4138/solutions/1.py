def count_correct_characters(s, t):
    assert len(s) == len(t)
    return sum(a == b for a, b in zip(s, t))
