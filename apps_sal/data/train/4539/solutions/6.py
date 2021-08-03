def hop_across(lst):
    count = 0
    i = 0
    while i <= len(lst) - 1:
        i += lst[i]
        count += 1
    i = len(lst) - 1
    while i >= 0:
        i -= lst[i]
        count += 1
    return count
