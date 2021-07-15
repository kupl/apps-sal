def encoder(data):
    dicto, store, i, f = {0: ""}, "", 0, ""
    save = 0
    while i <= len(data):
        if i == len(data) and store in list(dicto.values()):
            for k in dicto:
                if dicto[k] == store and store != "":
                    f += f"{k}"
            return f
        if store not in list(dicto.values()) and store != "":
            dicto[max(dicto.keys())+1] = store
            f += f"{save}{data[i-1]}"
            store = ""
            if i == len(data):
                return f
            continue
        if data[i] not in list(dicto.values()) and store == "":
            save = 0
            for m in dicto:
                if dicto[m] == store:
                    save = m
            dicto[max(dicto.keys())+1] = data[i]
            f += f"{save}{data[i]}"
            i += 1
        else:
            for m in dicto:
                if dicto[m] == store:
                    save = m
                elif dicto[m] == data[i] and store == "":
                    save = m
            store += data[i]
            i += 1
    return f


def decoder(data):
    dc, dic = "", {0: ""}
    i = 0
    while i <= len(data)-1:

        if data[i].isdigit() and i == len(data)-1:
            dc += dic[int(data[i])]
            return dc
        if data[i] == "0":
            dc += data[i+1]
            dic[max(dic.keys())+1] = data[i+1]
            i += 1
        elif data[i] != "0" and data[i].isdigit() and not data[i+1].isdigit():
            c = dic[int(data[i])]+data[i+1]
            dc += c
            dic[max(dic.keys())+1] = c
            i += 1
        elif data[i].isdigit() and data[i+1].isdigit():
            acc = data[i]
            while data[i+1].isdigit():
                i += 1
                acc += data[i]
                if i+1 == len(data):
                    dc += dic[int(acc)]
                    return dc
            dc += dic[int(acc)]+data[i+1]
            dic[max(dic.keys())+1] = dic[int(acc)]+data[i+1]
            i += 1
        else:
            i += 1

    return dc


