def remove_vowels(s):
    d=list(s)
    i=-1
    for c in s:
        i+=1
        if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
           d.remove(c)
    print(d)
    return "".join(d)
