def play_pass(s, n):
    shiftText = ''
    for char in s:
        if char.isdigit():
            shiftText += str(9 - int(char))
        elif char.isalpha():
            shifted = ord(char.lower()) + n
            shiftText += chr(shifted) if shifted <= ord('z') else chr(shifted - 26)
        else:
            shiftText += char
    caseText = ''
    for i in range(len(shiftText)):
        caseText += shiftText[i].upper() if i % 2 == 0 else shiftText[i].lower()
    return caseText[::-1]
