import string as Str


def decipher_this(string):

    allLetters = Str.ascii_letters
    allNumbers = Str.digits

    sentence = string.split(" ")

    decodedSentence = ""

    for word in sentence:
        ascii_code = word.strip(allLetters)
        ascii_letters = word.strip(allNumbers)

        first_letter = chr(int(ascii_code))

        if len(ascii_letters) > 1:
            ascii_letters = ascii_letters[-1:] + ascii_letters[1:-1] + ascii_letters[:1]

        decodedSentence = decodedSentence + first_letter + ascii_letters + " "

    return decodedSentence[:-1]
