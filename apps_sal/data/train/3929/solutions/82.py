def reverse(st):
    x = list()
    for i in st.split():
        x.append(i)
    x.reverse()
    temp = ""
    for i in x:
        temp += i + " "
    temp = temp.strip()
    return temp
