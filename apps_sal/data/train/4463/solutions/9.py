import string


def alphabet_position(text):
    lower_case_text = text.lower()
    alphabet = string.ascii_lowercase
    number = list(range(1, 27))
    dict_alphabet_number = dict(list(zip(alphabet, number)))
    collector = []
    for element in lower_case_text:
        if element in alphabet:
            collector.append(str(dict_alphabet_number[element]))
    return ' '.join(collector)
