def pig_it(text):
    n = 0
    x = 0
    text = text.split()
    text = list(text)
    pig_text = []
    for word in text:
        a = list(word)
        print(a)
        if len(a) > 1:
            a.append(a[0])
            del a[0]
            a.append('ay')
        if '!' in a:
            n += 1
        elif '?' in a:
            x += 1
        elif len(a) == 1:
            print(a)
            a.append('ay')
        a = ''.join(a)
        pig_text.append(a)
    pig_text = ' '.join(pig_text)
    return pig_text
