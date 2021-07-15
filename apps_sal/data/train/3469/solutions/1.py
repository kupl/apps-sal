def count_consonants(text):
    return len(set(filter(str.isalpha,text.lower())) - set("aeiou"))
