def cipher(phrase: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = [phrase[0]]
    for i, char in enumerate(phrase[1:]):
        if char != ' ':
            res.append(alphabet[(ord(char) - 97 + i // 3 + (i + 1) % 3) % 26])
        else:
            res.append(' ')
    return "".join(res)
