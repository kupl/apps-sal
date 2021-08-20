def decipher(cipher):
    answer = ''
    while cipher:
        l = 3 if cipher[0] == '1' else 2
        answer += chr(int(cipher[:l]))
        cipher = cipher[l:]
    return answer
