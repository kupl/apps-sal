def reverse_letter(string):
    out = []
    for n in range(len(string)):
        if string[n].isalpha():
            out.insert(0, string[n])
    return ''.join(out)
