def array(string):
    if len(string) <= 4 or len(" ".join(string.split(",")[1:-1])) == 0:
        return None
    else:
        return " ".join(string.split(",")[1:-1])
