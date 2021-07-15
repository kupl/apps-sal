def dollar_to_speech(value):
    if value[1] == "-":
        return "No negative numbers are allowed!"

    dot = value.index(".")
    dollars, cents = map(int, value[1:].split("."))
    end_d = "" if dollars == 1 else "s"
    end_c = "" if cents == 1 else "s"

    if dollars and cents:
        return "{} dollar{} and {} cent{}.".format(
            str(dollars), end_d, str(cents), end_c
        )
    elif cents and not dollars:
        return "{} cent{}.".format(str(cents), end_c)
    else:
        return "{} dollar{}.".format(str(dollars), end_d)
