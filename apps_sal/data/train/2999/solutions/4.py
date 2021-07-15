def hex_word_sum(string):
    string = string.upper().replace('S', '5')
    string = string.replace('O', '0')
    sum = 0
    for word in string.split(' '):
        try:
            sum += int(word.strip(), 16)
        except:
            pass
    return sum
