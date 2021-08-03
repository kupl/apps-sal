def remove_exclamation_marks(s):
    no_mark = ""

    for word in s:
        if word != "!":
            no_mark += word

    return no_mark
