def get_section_id(scroll, sizes):
    for i, _ in enumerate(sizes):
        if scroll < sum(sizes[:i + 1]):
            return i
    return -1
