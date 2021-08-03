def contamination(text, char):
    if not text or not char:
        return ''

    for ch in text:
        text = text.replace(ch, char)

    return text
