def reverse_letter(string):
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    a = list(string)
    new = []
    for k in range(0,len(a)):
        if a[k] in alphabet:
            new.append(a[k])
    
    b = list(range(0,len(new)))
    
    for i in range(0,len(new)):
        b[i] = new[len(new)-1-i]
    
    out = ""
    for j in range(0,len(new)):
        out += str(b[j])
    return out


