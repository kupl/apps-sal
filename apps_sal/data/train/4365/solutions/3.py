def is_isogram(string):
    char_dict = {}
    string = string.lower()
    for char in string:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    for key in char_dict:
        if char_dict[key] > 1:
            return False
    return True
