def name_in_str(str, name):
    it = iter(str.lower())
    return all(c in it for c in name.lower())
