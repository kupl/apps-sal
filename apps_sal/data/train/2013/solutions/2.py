def shift():
    word = input()
    i = 0
    shifted = ''
    while i < len(word) - 1:
        if word[i] != 'a':
            break
        shifted += word[i]
        i += 1
    if i == len(word) - 1 and word[i] == 'a':
        shifted += 'z'
        return shifted
    while i < len(word):
        if word[i] == 'a':
            shifted += word[i:]
            break
        shifted += chr(ord(word[i]) - 1)
        i += 1
    return shifted


print(shift())
