def encrypt(text, n):
    print('dasd')
    if n <= 0:
        return text
    new_str = text
    temp_str = ''
    for x in range(n):
        if len(new_str) % 2 == 1:
            iter_for_array_1 = 1
            iter_for_array_2 = 0
            temp_str = ''
            for z in range(int(len(new_str) / 2)):
                temp_str += new_str[iter_for_array_1]
                iter_for_array_1 += 2
            for z in range(int(len(new_str) / 2) + 1):
                temp_str += new_str[iter_for_array_2]
                iter_for_array_2 += 2
            new_str = temp_str
        else:
            iter_for_array_1 = 1
            iter_for_array_2 = 0
            temp_str = ''
            for z in range(int(len(new_str) / 2)):
                temp_str += new_str[iter_for_array_1]
                iter_for_array_1 += 2
            for z in range(int(len(new_str) / 2)):
                temp_str += new_str[iter_for_array_2]
                iter_for_array_2 += 2
            new_str = temp_str
    return new_str


def decrypt(encrypted_text, n):
    print(1)
    if n <= 0 or encrypted_text == '':
        return encrypted_text
    new_str = encrypted_text
    for x in range(n):
        a = int(len(encrypted_text) / 2)
        str1 = new_str[:a]
        str2 = new_str[a:]
        new_str = ''
        for new_X in range(a):
            new_str += str2[new_X]
            new_str += str1[new_X]
        if len(encrypted_text) % 2 == 1:
            new_str += str2[-1]
    return new_str
