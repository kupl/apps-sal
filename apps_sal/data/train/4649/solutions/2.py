def get_section_id(scroll, sizes):
    if scroll >= sum(sizes):
        return -1
    return sum(scroll >= sum(sizes[:i + 1]) for i in range(len(sizes)))
