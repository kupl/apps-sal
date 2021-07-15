def replace_dots(str):
    if "." in str:
        return str.replace(".", "-")
    elif not str:
        return ""
    else:
        return "no dots"
