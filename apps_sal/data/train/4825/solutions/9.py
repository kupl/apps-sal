def decrypt(test_key):
    alphabet = ["a", "b", "c", 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    key = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in alphabet:
        index = alphabet.index(i)
        key[index] = str(test_key.count(i))
    return "".join(key)
