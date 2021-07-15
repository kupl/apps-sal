def charCheck(text, mx, spaces):
    if not spaces:
        text = text.replace(' ', '')
    return [len(text) <= mx, text[:mx]]
