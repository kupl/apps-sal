def is_sorted_and_how(BLM):
    if BLM == sorted(BLM):
        return 'yes, ascending'
    if BLM == sorted(BLM)[::-1]:
        return 'yes, descending'
    return 'no'
