def make_password(phrase):
    new = ""
    phrase = phrase.replace("i", "1").replace("I", "1")
    phrase = phrase.replace("o", "0").replace("O", "0")
    phrase = phrase.replace("s", "5").replace("S", "5")
    phrase = phrase.split(" ")
    for i in phrase:
        new += i[0]
    return new
