def nerdify(txt):

    s = ""

    for i in range(len(txt)):

        if txt[i] == "a" or txt[i] == "A":

            s += '4'

        elif txt[i] == "e" or txt[i] == "E":

            s += '3'

        elif txt[i] == 'l':

            s += '1'

        else:

            s += txt[i]

    return s
