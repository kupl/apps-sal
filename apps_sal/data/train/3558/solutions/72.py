def capitalize_word(word):
    return ' '.join(word[:1].upper() + word[1:] for word in word.split(' ')) 

print(capitalize_word("hello"))
