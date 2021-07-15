def find_missing_letter(chars):
    return [chr(n) for n in range(ord(chars[0]),ord(chars[-1])+1) if n not in [ord(c) for c in chars]][0]
    


