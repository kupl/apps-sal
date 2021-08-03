def reverse_words(text):
  # go for it
    spl = text.split(" ")
    new = ''
    for i in spl:
        new += i[::-1] + " "
    return new.strip()
