def find_page_number(pages):
    (n, res) = (1, [])
    for p in pages:
        if p == n:
            n += 1
        else:
            res.append(p)
    return res
