def frame(text, char):
    length = len(max(text, key=len))
    start = end = char * (length + 3)
    k = [' ' + x + ' ' * (length - len(x) + 1) for x in text]
    return (char + '\n' + char).join([start] + k + [end])
