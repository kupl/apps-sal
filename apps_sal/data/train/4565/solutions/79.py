def replace_dots(str):
    return "".join([x if x != "." else "-" for x in str])
