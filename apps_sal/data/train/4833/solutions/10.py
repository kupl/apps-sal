def replace_exclamation(s):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in range(len(vowels)):
        s=s.replace(vowels[i],"!")
    return s
