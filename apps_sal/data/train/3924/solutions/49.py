def reverse_words(text):
    lst = text.split(" ")
    lst = [i[::-1] for i in lst]
    return " ".join(lst)
