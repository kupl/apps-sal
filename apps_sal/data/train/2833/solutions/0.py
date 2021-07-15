def sect_sort(lst, start, length=0):
    end = start + length if length else len(lst)
    return lst[:start] + sorted(lst[start:end]) + lst[end:]
