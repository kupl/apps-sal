import string


def string_letter_count(s):
    alphabet = string.ascii_lowercase
    sts = s.strip(" ").lower()
    result = ""
    for i in alphabet:
        if i in sts:
            result += "%s%s" % (sts.count(i), i)

    return result
