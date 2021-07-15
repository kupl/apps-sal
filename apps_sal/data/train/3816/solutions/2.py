def move_ten(stg):
    return "".join(chr(97 + ((ord(c) - 87) % 26)) for c in stg)
