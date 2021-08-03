def duplicate_count(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count
