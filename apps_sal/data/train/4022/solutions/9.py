import re


def soundex(name):
    sounds = []
    namelist = name.split()

    for namey in namelist:
        firstletter = namey[0].upper()
        temp = namey.lower()
        temp = re.sub('[hw]', "", temp)
        temp = re.sub('[aeiouy]', "*", temp)
        temp = re.sub('[bfpv]', "1", temp)
        temp = re.sub('[cgjkqsxz]', "2", temp)
        temp = re.sub('[dt]', "3", temp)
        temp = re.sub('[l]', "4", temp)
        temp = re.sub('[mn]', "5", temp)
        temp = re.sub('[r]', "6", temp)
        temp = re.sub(r'(.)\1+', r'\1', temp)

        if firstletter in ["H", "W"]:
            tempcode = firstletter + temp + "0000"
        else:
            tempcode = firstletter + temp[1:] + "0000"
        tempcode = re.sub("[*]", "", tempcode)

        sounds.append(tempcode[0:4])

    return " ".join(sounds)
