def pete_talk(speech, ok = []):
    from re import split, sub
    ok = [x.lower() for x in ok]
    
    def add_stars(strng):
        x = strng.group(0)

        if x.lower() not in ok:
            return x[0] + "*"*(len(x) - 2) + x[-1]
        else:
            return x
    
    def process(s):
        s = sub("^([a-z])", lambda x: x.group(0).upper(), s)
        s = sub("(?<=.{1})\w", lambda x: x.group(0).lower(), s)
        s = sub("[a-zA-Z]{3,}", add_stars, s)
        return s

    return " ".join(process(s) for s in split("(?<=[.!?])\ ", speech))
