def array(string):
    string = ' '.join(string.split(",")[1:-1])
    if string:
        return string.strip()
    else:
        return None
