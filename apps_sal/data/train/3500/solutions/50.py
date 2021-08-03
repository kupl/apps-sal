def remove_exclamation_marks(s):
    return s.replace("!", "")


def remove_exclamation_marks(s):
    return "".join(char for char in s if char != "!")


def remove_exclamation_marks(s):
    final_s = []
    for char in s:
        if char != "!":
            final_s.append(char)
    return "".join(final_s)


def remove_exclamation_marks(s):
    print(("x", s, "x"))
    i_compensation = 0
    s = list(s)
    for i in range(len(s)):
        print(("before", i))
        if s[i - i_compensation] == "!":
            s.pop(i - i_compensation)
            i_compensation += 1
    return "".join(s)
