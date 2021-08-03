def timed_reading(max_length, text):
    count = 0
    for punctuation_mark in '!.,?\'\"_-)(':
        text = text.replace(punctuation_mark, '')
    listed_text = text.split(" ")

    for word in listed_text:
        if len(word) <= max_length and len(word) > 0:
            count += 1
    return count


print(timed_reading(4, "The Fox asked the stork, 'How is the soup?'"))
