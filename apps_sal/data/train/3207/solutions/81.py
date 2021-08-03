def reverseWords(s):
    x = [x for x in s.split(" ")]
    return "".join(x + " " for x in x[::-1])[:-1]
