def replace_dots(str):
    if "." in str:
        return str.replace(".","-")
    elif str == "no dots":
        return "no dots"
    else:
        return ""
