def reverseWords(str):
    str = str.split()
    str = reversed(str)
    return " ".join(str)
