def dollar_to_speech(s):
    d, c = map(int, s[1:].split("."))
    ds, cs = f"{d} dollar" + "s"*(d != 1), f"{c} cent" + "s"*(c != 1)
    return "No negative numbers are allowed!" if d < 0 else f"{ds}." if c == 0 else f"{cs}." if d == 0 else f"{ds} and {cs}."
