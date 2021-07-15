def reverse_words(text):
    reversed = ""
    for word in text.split(" "):
        w =" "
        for char in word:
            w = char + w
        reversed = reversed + w
    return (reversed.strip())
