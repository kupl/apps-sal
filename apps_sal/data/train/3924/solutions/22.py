def reverse_words(str):
    lst = str.split(" ")
    for i in range(len(lst)):
        lst[i] = lst[i][::-1]
    return ' '.join(lst)

