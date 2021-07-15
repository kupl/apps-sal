def encrypt(text,key):
    k = [ord(i) - 97 for i in key]
    text = ''.join(c for c in text if c.isalpha())
    text = text.upper() + "Z"*(len(text) % 2)
    nums = [ord(c) - 65 for c in text]
    Out = ''
    for i, j in zip(nums[::2],nums[1::2]):
        Out += chr((k[0]*i + k[1]*j)%26 + 65) + chr((k[2]*i + k[3]*j)%26 + 65)
    return Out
