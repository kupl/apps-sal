def reverse_words(text):
    spl = text.split(" ")
    new = ''
    for i in spl:
        new += i[::-1] + " "
    return new.strip()
