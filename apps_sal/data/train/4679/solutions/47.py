def to_freud(sentence):
    res = ""
    my_list = sentence.split(' ')
    for i in range(len(my_list)):
        res += "sex "
    return res[:-1]
