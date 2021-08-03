def count_correct_characters(a, b):
    return len([i for i in range(len(a)) if a[i] == b[i]]) if len(a) == len(b) else error
