def name_in_str(str, name):
    name = list(name.lower())[::-1]
    charFind = name.pop();
    for x in str.lower():
        if(x == charFind):
            if(len(name) == 0):
                return True;
            charFind = name.pop();
    return False;
        

