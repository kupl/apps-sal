def charCheck(text, mx, spaces):
    text = text if spaces else text.replace(' ', '')
    return [len(text) <= mx, text[:mx]]
