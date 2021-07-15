def array(string):
    mod = string.replace(',', ' ').split()
    if len(mod) < 3:
        return None
    return ' '.join(mod[1:-1])
