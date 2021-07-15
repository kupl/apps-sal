def lottery(s):
    buffer = []
    for char in s:
        if char.isdigit() and char not in buffer:
            buffer.append(char)
    if buffer:
        return ''.join(buffer)
    else:
        return 'One more run!'
