def find_missing_letter(chars):
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    match = False
    count = 0
    for letter in s:
        if letter == chars[count]:
            match = True
            count = count + 1
        elif match == True:
            return letter
