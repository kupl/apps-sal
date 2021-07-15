def replace_exclamation(s):
    vowels=['a','e','i','o','u']
    for i in s:
        if i.lower() in vowels:
            s=s.replace(i,"!")
    return s
