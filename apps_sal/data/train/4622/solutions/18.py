def double_check(strng):
    prev_char = strng[0]
    for char in strng[1:].lower():
        if char == prev_char:
            return True
        prev_char = char
    return False
