s = "zero one two three four five six seven eight nine"
ls = s.split(" ")


def numbers_of_letters(n):
    t = [stringa(n)]
    while n != len(stringa(n)):
        n = len(stringa(n))
        t.append(stringa(n))
    return t


def stringa(n):
    return "".join([ls[int(i)] for i in str(n)])
