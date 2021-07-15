abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def caesar_crypto_encode(text, shift):
    if not text or text in ' '*10: return ''
    s=''
    for i in text:
        if i.isalpha():
            s += abc[(abc.index(i)+shift)%52]
        else:
            s += i
    return s
