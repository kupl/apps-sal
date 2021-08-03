def string_letter_count(s):
    s = s.lower()
    split = list(s)
    split.sort()
    string = ""
    for i in split:
        if i >= 'a' and i <= 'z' and i not in string:
            string = string + str(split.count(i))
            string += i
    return string
