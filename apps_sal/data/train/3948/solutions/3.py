def sel_reverse(lst, k):
    return sum((lst[i:i + k][::-1] for i in range(0, len(lst), k)), []) if k else lst
