def find_page_number(pages):
    arr, l = [], 0
    for i, p in enumerate(pages, 1):
        if p != i - l:
            arr.append(p)
            l += 1
    return arr
