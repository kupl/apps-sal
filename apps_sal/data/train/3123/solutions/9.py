def count_repeats(txt):
    prev = None
    removed_chars = 0
    for ch in txt:
        if ch == prev:
            removed_chars += 1
        prev = ch
    return removed_chars
