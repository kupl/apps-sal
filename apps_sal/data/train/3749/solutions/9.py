def expanded_form(num):
    return " + ".join(str(num)[i] + "0" * ( len(str(num)) - i - 1 ) for i in range(len(str(num))) if str(num)[i] != "0")
