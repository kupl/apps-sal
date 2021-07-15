def get_textliterals(pv_code):
    start_index = None
    all_index_store = []
    a_comment = False
    b_comment = False
    for index, char in enumerate(pv_code):
        if char == '*' and pv_code[index - 1] == '/':
            a_comment = True
        elif a_comment == True and char == '/' and pv_code[index - 1] == '*':
            a_comment = False
        elif char == '-' and pv_code[index - 1] == '-':
            b_comment = True
        elif b_comment == True and char == '\n':
            b_comment = False
        elif (char == '\'' or len(pv_code) - 1 == index) and a_comment == False and b_comment == False:
            if start_index != None:
                if (index > 0 and pv_code[index - 1] == '\'') or (len(pv_code) > index + 1 and pv_code[index + 1] == '\''):
                    continue
                all_index_store.append((start_index, index + 1))
                start_index = None
            else:
                start_index = index
    return all_index_store
            

