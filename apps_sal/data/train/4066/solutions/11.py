def string_to_array(s):
    lst = []
    split_s = s.split()
    if s == "":
        lst.append("")
    for letter in split_s:
        lst.append(letter)
    return lst
