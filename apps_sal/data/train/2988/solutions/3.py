def reverse_and_combine_text(text):
    array = text.split(' ')
    while len(array) > 1:
        temp = []
        for i in range(0, len(array), 2):
            try:
                temp.append(array[i][::-1] + array[i + 1][::-1])
            except IndexError:
                temp.append(array[i][::-1])
        array = temp
    return ''.join(array)
