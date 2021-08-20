def simple_transposition(text):
    even_idx = ''
    odd_idx = ''
    for (idx, char) in enumerate(text):
        if idx % 2 == 0:
            even_idx += char
        else:
            odd_idx += char
    new_text = even_idx + odd_idx
    return new_text
