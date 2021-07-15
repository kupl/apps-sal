def play_pass(phrase, n):
    output = ''
    for i, char in enumerate(phrase):
        if char.isdigit():
            char = str(9 - int(char))
        elif char.isalpha():
            code = (ord(char) - 65 + n) % 26
            char = chr(code + 65)
        if i & 1:
            char = char.lower()
        output = char + output
    return output
