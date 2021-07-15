def to_alternating_case(string):
    string2=''
    for i in string:
        if i.upper()==i:
            string2+=i.lower()
        else:
            string2+=i.upper()
    return string2
