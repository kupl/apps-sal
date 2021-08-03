def get_section_id(scroll, sizes):
    a = 0
    for i in sizes:
        scroll -= i

        if scroll < 0:
            return a
        a += 1
    return -1
