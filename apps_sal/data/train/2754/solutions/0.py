lm = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
ll = "abcdefghijklmnopqrstuvwxyz0123456789"
repldict = {'.-': 'a', '-...': 'b'}

for i in range(2, len((ll))):
    repldict.update({lm[i]: ll[i]})
print(repldict)


def decode(encoded):
    if encoded == " " or encoded == "":
        return encoded
    words = encoded.split("  ")
    engwords = []
    for word in words:
        engword = []
        letters = word.split(" ")
        for letter in letters:
            engword.append(repldict.get(letter))
        engword.append(" ")
        engwords.append("".join(engword))
    r = "".join(engwords)
    return r[0:len(r) - 1]
