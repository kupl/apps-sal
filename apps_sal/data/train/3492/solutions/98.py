import ast


def correct_polish_letters(st):
    letters = """ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z"""
    letters = "{'" + letters.replace(" -> ", "':'").replace(",", "',").replace("\n", "'") + "'}"
    letters = ast.literal_eval(letters)
    st2 = ""
    for i in range(len(st)):
        if st[i] not in letters:
            st2 += st[i]
        else:
            st2 += letters.get(st[i])
    return st2
