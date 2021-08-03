def charCheck(text, mx, spaces):
    if spaces == False:
        text = text.replace(" ", "")

    return [len(text) <= mx, text[:mx]]
