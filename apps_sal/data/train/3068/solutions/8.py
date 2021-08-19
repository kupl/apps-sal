trans = str.maketrans('abcdeghjklmnopqrsuwxyz', 'vkbaapqstuvwnyzabpfghi')


def vowel_back(st):
    return st.translate(trans)
