def reverse_number(n):
    number = str(n)
    list = []
    index = 0
    if n < 0:
        for i in number:
            if i.isdigit() == True:
                list.insert(0, i)

            new_num = "".join(list)
        return(0 - int(new_num))
    else:
        for i in number:
            if i.isdigit() == True:
                list.insert(0, i)
        for i in list:
            while i == 0:
                index += 1
            else:
                break
        new_num = "".join(list[index::])
        return (int(new_num))
