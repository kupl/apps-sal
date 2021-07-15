def repeat_str(repeat, string):
    repeated_words = ""
    for i in range(repeat):
        repeated_words += string
    return repeated_words

repeat_str(5, "a")
