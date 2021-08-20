def words_to_marks(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    my_list = list(s)
    summ = 0
    for x in range(len(my_list)):
        for y in range(len(alphabet)):
            if my_list[x] == alphabet[y]:
                summ += y + 1
    return summ
