def position(alphabet):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(26):
        if alph[i] == alphabet: return "Position of alphabet: " + str(i+1)
