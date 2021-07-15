def get_section_id(scroll, sizes):
    
    for i, s in enumerate(sizes):
        scroll -= s
        if scroll < 0:
            return i
    
    return -1
