def no_space(x):
    new_sen = ""
    character_num = 0
    for chars in  x:
        if (x[character_num]) == " ":
            character_num = character_num + 1
        else:
            new_sen = new_sen + x[character_num]
            character_num = character_num + 1
    return new_sen
