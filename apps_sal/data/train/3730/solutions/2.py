def capitalize(s):
    word = ""
    output = []
    for n in range(0, len(s)):
        if n % 2 == 0:
            word = word + s[n].upper()
        else:
            word = word + s[n]
    output.append(word)
    output.append(word.swapcase())
    return output
