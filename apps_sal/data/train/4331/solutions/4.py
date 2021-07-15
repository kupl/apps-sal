def heavy_metal_umlauts(boring_text):
    rtext = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
    htext = ['Ä', 'Ë', 'Ï', 'Ö', 'Ü', 'Ÿ', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ']
    out = ''
    for i in boring_text:
        if i in rtext:
            out += htext[rtext.index(i)]
        else:
            out += i
    return out
