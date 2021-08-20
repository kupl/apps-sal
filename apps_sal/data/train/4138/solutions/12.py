def count_correct_characters(a, b):
    assert len(a) == len(b)
    return sum((a[i] == b[i] for i in range(len(a))))
