def get_section_id(scroll, sizes):
    where = 0
    for i in range(len(sizes)):
        where += sizes[i]
        if where > scroll:
            return i
    return -1
