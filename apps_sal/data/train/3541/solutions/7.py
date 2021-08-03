def find_page_number(pages):
    r = []
    i = 0
    while i < len(pages):
        if pages[i] != i + 1:
            r.append(pages.pop(i))
            i -= 1
        i += 1
    return r
