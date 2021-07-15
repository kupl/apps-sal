def reverseWords(s):
    spl = s.split(" ")
    x = spl[::-1]
    new =''
    for i in x:
        new+=i + " "
    return new.strip()

