def replace_dots(str):
    return __import__('re').sub(r"\.", "-", str)
