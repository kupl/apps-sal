from collections import deque
KEYBOARD = ['zxcvbnm,.', 'ZXCVBNM<>', 'asdfghjkl', 'ASDFGHJKL', 'qwertyuiop', 'QWERTYUIOP']


def encrypt(text, encryptKey): return converter(text, encryptKey, 1)
def decrypt(text, encryptKey): return converter(text, encryptKey, -1)


def converter(text, encryptKey, sens):
    deques = list(map(deque, KEYBOARD))
    for i, deq in enumerate(deques):
        deq.rotate(-sens * (encryptKey // 10**(i // 2) % 10))
    return text.translate(str.maketrans(''.join(KEYBOARD), ''.join(''.join(deq) for deq in deques)))
