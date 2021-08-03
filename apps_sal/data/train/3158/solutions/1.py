def one_down(txt):
    try:
        return ''.join('Z' if i == 'A' else 'z' if i == 'a' else chr(ord(i) - 1)
                       if i.isalpha() else i for i in txt)
    except:
        return "Input is not a string"
