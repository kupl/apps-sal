def hex_to_dec(s):
    heshion = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

    tal = 0

    for x in range(0, len(s)):
        tal += heshion[s[x]] * 16**(len(s) - 1 - x)

    return(tal)
