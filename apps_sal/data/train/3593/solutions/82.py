def capitalize(chars, indices):
    for index in indices:
        if index < len(chars):
            chars = chars[0:index] + chars[index].capitalize() + chars[index+1:]
    return chars

