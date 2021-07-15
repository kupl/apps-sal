def alternateCase(s):
    new_text=''
    for i in s:
        if i.islower():
            new_text+=i.upper()
        else:
            new_text+=i.lower()
    return new_text
