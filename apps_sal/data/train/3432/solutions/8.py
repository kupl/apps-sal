def cipher(phrase: str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = [phrase[0]]
    for i, char in enumerate(phrase[1:]):
        if char != ' ':
            res.append(alphabet[(ord(char)-97 + i//3 + (i+1)%3) % 26])
        else:
            res.append(' ')
    return "".join(res)
    #0, 1,2,0, 2,3,1, 3,4,2,4,5,3,5,6,4,6,7,5,7,8,

