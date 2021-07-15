def array(string):
    items = string.split(",")[1:-1]
    return " ".join(items) if len(items)>0 else None

