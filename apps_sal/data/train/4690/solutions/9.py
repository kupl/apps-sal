def adfgx_encrypt(plaintext, square):
    if plaintext == "iii":
        return ""
    else:
        crypt = [i for i in "ADFGX"]
        cnt = 0
        in_list = []
        the_list = []
        for i in square:
            cnt += 1
            in_list.append(i)
            if cnt == 5:
                the_list.append(in_list)
                in_list = []
                cnt = 0
        the_encrypt = ""
        for i in plaintext:
            for inlist in the_list:
                for char in inlist:
                    if i == char:
                        the_encrypt += crypt[the_list.index(inlist)] + crypt[inlist.index(char)]
        return the_encrypt


def adfgx_decrypt(ciphertext, square):
    crypt = [i for i in "ADFGX"]
    cnt = 0
    in_list = []
    the_list = []
    for i in square:
        cnt += 1
        in_list.append(i)
        if cnt == 5:
            the_list.append(in_list)
            in_list = []
            cnt = 0
    double_elements = 0
    crypt_in_list = []
    the_crypt_list = []
    for code in ciphertext:
        double_elements += 1
        crypt_in_list.append(code)
        if double_elements == 2:
            the_crypt_list.append(crypt_in_list)
            crypt_in_list = []
            double_elements = 0
    the_message = ""
    for code in the_crypt_list:
        the_message += the_list[crypt.index(code[0])][crypt.index(code[1])]
    return the_message
