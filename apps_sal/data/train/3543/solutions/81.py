def increment_string(strng: str):
    number = ''
    for letter in strng[::-1]:
        if letter.isdigit():
            number = letter + number
        else:
            break
    if not number:
        return strng + '1'
    result = str(int(number) + 1)
    result = '0' * (len(number) - len(result)) + result
    return strng[:len(strng) - len(number)] + result
