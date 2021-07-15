def alternateCase(s):
    new=""
    for i in range(len(s)):
        if s[i].islower():
            new+=s[i].upper()
        if s[i].isupper():
            new+=s[i].lower()
        if s[i]==" ":
            new+=" "
    return new
