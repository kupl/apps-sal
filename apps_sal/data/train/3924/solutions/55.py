def reverse_words(text: str) -> str:
    # go for it
    final: str = ''
    string_list: list = text.split(' ')
    for i in string_list[:-1]: #go on each word and reverse before last one
        final += i[::-1] + ' ' #add space where needed
    final += string_list[-1][::-1] #add the last word reversed
    return final
