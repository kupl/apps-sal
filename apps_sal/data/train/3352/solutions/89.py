def find_longest(arr):
    longest_len = 0
    longest = None
    for el in arr:
        sample_len = len(str(el))
        if sample_len > longest_len:
            longest_len = sample_len
            longest = el
    return longest
