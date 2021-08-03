def vert_mirror(strng):
    lines = strng.split("\n")
    transformed_lines = ["".join(reversed(line)) for line in lines]
    return "\n".join(transformed_lines)


def hor_mirror(strng):
    lines = strng.split("\n")
    return "\n".join(reversed(lines))


def oper(fct, s):
    return fct(s)
