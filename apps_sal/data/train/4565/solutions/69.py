def replace_dots(str):
    output = ""
    for element in str:
        if element == ".":
            output += "-"
        else:
            output += element
    return output
