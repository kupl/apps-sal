def kebabize(string):
    a = ''
    for i in string:
        if i.isupper():
            a += '-' + i.lower()
        if i.islower():
            a += i
    return a.strip('-')
    # your code here
