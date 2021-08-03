def reverse_letter(string):
    new = [s for s in string if s.isalpha()]
    a = new
    a.reverse()
    return ''.join(list(a))
