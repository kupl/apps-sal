def hex_word_sum(string):
    sum = 0
    for word in string.upper().replace('S', '5').replace('O', '0').split(' '):
        try:
            sum += int(word.strip(), 16)
        except:
            pass
    return sum
