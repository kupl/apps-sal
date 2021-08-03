def align_right(text, width):
    answer = []
    splitted = text.split(' ')
    temp = ''
    i = 0
    while i < len(splitted):
        while i < len(splitted) and len(temp + splitted[i]) < width + 1:
            temp += splitted[i] + ' '
            i += 1
        temp = temp.strip()
        answer.append(' ' * (width - len(temp)) + temp)
        temp = ''
    return '\n'.join(answer)
