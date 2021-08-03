
def string_letter_count(s):
    return "".join(str(s.count(i.lower()) + s.count(i.upper())) + i for i in sorted(set(list(s.lower()))) if i.isalpha())
