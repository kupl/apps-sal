import ast


def correct_polish_letters(st):
    letters = 'ą -> a,\nć -> c,\nę -> e,\nł -> l,\nń -> n,\nó -> o,\nś -> s,\nź -> z,\nż -> z'
    letters = "{'" + letters.replace(' -> ', "':'").replace(',', "',").replace('\n', "'") + "'}"
    letters = ast.literal_eval(letters)
    st2 = ''
    for i in range(len(st)):
        if st[i] not in letters:
            st2 += st[i]
        else:
            st2 += letters.get(st[i])
    return st2
