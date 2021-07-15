def reverse(st):
    list=st.split()
    list.reverse()
    for i in range(1,len(list)*2-1,2):
        list.insert(i," ")
    string=""
    for i in list:
        string+=i
    return string
    

