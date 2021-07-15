def boolean_to_string(b):
    if type(b) == type(True) and b == True:
        return ("True")
    else:
        return ("False")

print((boolean_to_string(False)))

