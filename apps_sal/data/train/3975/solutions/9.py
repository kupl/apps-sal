def find_missing_letter(chars):
    next = chars[0]
    for letter in chars: 
        if letter != next: return next
        next = chr(ord(letter) + 1)
    return 0


