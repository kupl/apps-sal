def reverse_letter(string):
    return ''.join(s for s in reversed(string) if s.isalpha())
