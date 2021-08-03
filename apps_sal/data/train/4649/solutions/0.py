def get_section_id(scroll, sizes):
    c = 0
    for idx, s in enumerate(sizes):
        c += s
        if scroll < c:
            return idx
    return -1
