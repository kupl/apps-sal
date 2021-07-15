def reverse(st):
    string_to_list = st.split()
    reversed_list = string_to_list.reverse()
    list_to_string = " ".join(string_to_list)
    print(("'"+list_to_string+"'"))
    return(list_to_string)

