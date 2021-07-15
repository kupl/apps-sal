def invite_more_women(arr):
    return len([a for a in arr if a == 1]) > len([a for a in arr if a == -1])
