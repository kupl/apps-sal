def string_clean(s):
    return "".join([s[i] for i in range(len(s)) if s[i].isnumeric() == False])
