def validBraces(string):
    while len(string) > 0:
        if "()" in string:
            string = string.replace("()", "")
        elif "[]" in string:
            string = string.replace("[]", "")
        elif "{}" in string:
            string = string.replace("{}", "")
        else:
            return False
    return True
