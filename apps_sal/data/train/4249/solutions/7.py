def base64_to_base10(string):
    return sum(["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".index(letter) * (64**power) for power, letter in enumerate(string[::-1])])
