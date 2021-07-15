def reverse(st):
    list_st = []
    for i in st.split():
        list_st.append(i)
    new_list = list_st[::-1]
    return ' '.join(new_list)
