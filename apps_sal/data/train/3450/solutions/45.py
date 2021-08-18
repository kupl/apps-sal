def array(string):
    if string.count(',') > 1:
        return " ".join(string.split(",")[1:-1]).strip()
    return None
