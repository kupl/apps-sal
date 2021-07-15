def hamster_me(code, message):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    output=''
    for char in message:
        try:
            codeLetter = max([c for c in sorted(code) if c <= char])
        except:
            codeLetter = max(code)
        codeIndex = alpha.index(codeLetter)
        charIndex = alpha.index(char)
        if codeIndex <= charIndex:
            appendNo = str(charIndex - codeIndex + 1)
        else:
            appendNo = str(charIndex + len(alpha) - codeIndex + 1)
        output += codeLetter + appendNo
    return output

