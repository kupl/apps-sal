def charCheck(text, mx, spaces):
    if spaces == True:
        return[len(text)<=mx, text[:mx]]
    else:
        t = text.replace(' ','')
        return[len(t)<=mx, t[:mx]]
