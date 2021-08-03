def capitalize_word(word):
    arr = []
    for i in range(len(word)):
        if i == 0:
            arr.append(word[0].upper())
        else:
            arr.append(word[i])
    return ''.join(arr)
