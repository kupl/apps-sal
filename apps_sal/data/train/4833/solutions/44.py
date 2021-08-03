def replace_exclamation(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    x = []
    for i in s:
        if i.lower() in vowels:
            x.extend("!")
        else:
            x.extend(i)
    return "".join(x)
