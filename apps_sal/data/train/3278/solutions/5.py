def string_expansion(s):
    strin = []
    multiplier = 1
    result = ""
    for letter in s:
        try:
           strin.append(int(letter))
        except ValueError:
            strin.append(letter)
    for i in strin:
        if isinstance(i, int):
            multiplier = i
        elif isinstance(i, str):
            result += multiplier * i
    return result
