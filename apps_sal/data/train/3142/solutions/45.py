def seven_ate9(txt):
    count = 0
    txt = list(txt)
    removeable = []
    for i in range(len(txt)):
        try:
            if txt[i - 1] == "7":
                if txt[i] == "9":
                    if txt[i + 1] == "7":
                        txt[i - 1], txt[i], txt[i + 1] = "7", "", "7"
        except IndexError:
            continue
    for i in txt:
        if i in removeable:
            txt.remove(txt[i])

    return "".join(txt)
