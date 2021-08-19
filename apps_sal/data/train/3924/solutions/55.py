def reverse_words(text: str) -> str:
    final: str = ''
    string_list: list = text.split(' ')
    for i in string_list[:-1]:
        final += i[::-1] + ' '
    final += string_list[-1][::-1]
    return final
