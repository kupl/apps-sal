def dollar_to_speech(value):
    if value[1] == "-":
        return "No negative numbers are allowed!"
    if value == "$0.00":
        return "0 dollars."
    
    output = []
    dollars, cents = map(int, value[1:].split("."))
    
    if dollars:
        output.append("%s dollar%s" % (dollars, "s" * (dollars != 1)))
    if cents:
        output.append("%s cent%s" % (cents, "s" * (cents != 1)))
    
    return " and ".join(output) + "."
