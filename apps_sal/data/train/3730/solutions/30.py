def capitalize(s):
    even = ""
    odd = ""
    for ind,char in enumerate(s):
        if ind%2 == 0:
            even += char.upper()
            odd += char
        elif ind%2 != 0:
            odd += char.upper()
            even += char
    return [even, odd]
