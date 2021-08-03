def position(alphabet):
    alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(0, 26):
        if alphabet == alph_list[i]:
            j = i + 1
            return "Position of alphabet: " + str(j)
