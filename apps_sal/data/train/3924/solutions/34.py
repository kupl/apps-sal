def reverse_words(str):
    ss = list("".join(i[::-1] for i in str.split())[::-1])
    return "".join([ss.pop() if el != " " else " " for el in str])
