def hex_word_sum(string):
    string = string.replace('O', '0')
    string = string.replace('S', '5')
    new = string.split()
    sum = 0
    for i in new:
        try:
            v = int(i, 16)
        except:
            v = 0
        sum = sum + v
    return sum
