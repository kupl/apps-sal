def replace_exclamation(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i].lower() == "a" or s_list[i].lower() == "e" or s_list[i].lower() == "i" or s_list[i].lower() == "o" or s_list[i].lower() == "u":
            s_list[i] = "!"
    string = ""
    for st in s_list:
        string += st
    return string
