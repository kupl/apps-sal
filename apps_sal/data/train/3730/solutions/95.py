def capitalize(s):
    even = ''
    odd = ''
    bigArr = []
    for i in range(len(s)) :
        if(i % 2 == 0) :
            even += s[i].upper()
            odd += s[i].lower()
        else:
            even += s[i].lower()
            odd += s[i].upper()
    return [even, odd]
