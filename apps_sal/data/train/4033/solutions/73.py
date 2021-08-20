def contamination(text, char):
    lt = list(text)
    for i in range(len(lt)):
        lt[i] = char
    return ''.join(lt)
