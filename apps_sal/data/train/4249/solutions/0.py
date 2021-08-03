DIGITS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_to_base10(string):
    return sum(DIGITS.index(digit) * 64**i
               for i, digit in enumerate(string[::-1]))
