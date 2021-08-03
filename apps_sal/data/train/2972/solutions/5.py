def multiple_split(s, delimiters=[]):
    if s == "":
        return []
    elif delimiters == []:
        return [s]

    return [w for w in s.translate("".maketrans("".join(delimiters), delimiters[0] * len(delimiters))).split(delimiters[0]) if w != ""]
