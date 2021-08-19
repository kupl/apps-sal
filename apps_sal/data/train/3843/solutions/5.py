template_chars_region = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;-?! '()$%&"
template_chars_region += '"'


def decrypt(encrypted_text):
    result = ''
    if not encrypted_text or 0 == len(encrypted_text):
        return encrypted_text
    template_length = len(template_chars_region)
    first_original_char = template_chars_region[template_length - template_chars_region.index(encrypted_text[0]) - 1]
    result = first_original_char
    for (index, single_char) in enumerate(''.join(encrypted_text[1:])):
        previous_template_index = template_chars_region.index(first_original_char)
        difference_template_index = template_chars_region.index(single_char)
        result += template_chars_region[(previous_template_index - difference_template_index + template_length) % template_length]
        first_original_char = result[-1]
    result_copy = ''
    for (index, single_char) in enumerate(result):
        if 0 != index % 2:
            if single_char.islower():
                single_char = single_char.upper()
            else:
                single_char = single_char.lower()
        result_copy += single_char
    result = result_copy
    return result


def encrypt(text):
    result = ''
    if not text or 0 == len(text):
        return text
    text_copy = ''
    template_length = len(template_chars_region)
    for (index, single_char) in enumerate(text):
        char_template_index = template_chars_region.index(single_char)
        if 0 != index % 2 and single_char.isalpha():
            if single_char.islower():
                single_char = single_char.upper()
            else:
                single_char = single_char.lower()
        text_copy += single_char
    for (index, char) in enumerate(text_copy):
        if 0 == index:
            continue
        previous_template_index = template_chars_region.index(text_copy[index - 1])
        current_template_index = template_chars_region.index(text_copy[index])
        result += template_chars_region[(previous_template_index - current_template_index + template_length) % template_length]
    result = template_chars_region[template_length - template_chars_region.index(text[0]) - 1] + result
    return result
